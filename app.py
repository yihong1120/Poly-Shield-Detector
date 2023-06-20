from PySide6.QtWidgets import QMainWindow, QFileDialog, QGraphicsPixmapItem, QApplication, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsScene, QGraphicsOpacityEffect, QGraphicsPolygonItem, QMenu
from PySide6.QtGui import QImage, QPixmap, QIcon, QBrush, QColor, QPen, QPolygonF,QTransform, QAction
from PySide6.QtCore import Qt, QPointF
import json
from collections import Counter
from shapely.geometry import Polygon, box
from imageprocess_ui import Ui_MainWindow
from detection_predictor import DetectionPredictor, class_names
import sys
import os


class CustomGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None, mainWindow=None):
        super().__init__(parent)
        self.mainWindow = mainWindow  
        self.pointItems = {}  # QGraphicsEllipseItems for the points
        self.lineItems = {}  # QGraphicsLineItems for the lines
        self.points = []  #points for the polygon
        self.close_poly = None
        self.closed_polygons = []

    def contextMenuEvent(self, event):
        # get selected item
        # item = self.itemAt(event.scenePos(), Qt.IdentityTransform)
        item = self.itemAt(event.scenePos(), QTransform.fromTranslate(0, 0))


        # check if item is a polygon
        if isinstance(item, QGraphicsPolygonItem):
            # create context menu
            contextMenu = QMenu(self.mainWindow)

            # create actions
            editAction = QAction("Edit", self.mainWindow)
            deleteAction = QAction("Delete", self.mainWindow)

            # add actions to menu
            contextMenu.addAction(editAction)
            contextMenu.addAction(deleteAction)

            # connect actions
            editAction.triggered.connect(lambda: self.edit_polygon(item))
            deleteAction.triggered.connect(lambda: self.delete_polygon(item))

            # show menu
            contextMenu.exec(event.screenPos())

    def edit_polygon(self, polygon):
        # edit polygon code here
        print("Editing polygon")

    def remove_point(self, point_key):
        self.mainWindow.view_image_ploygon.scene().removeItem(self.pointItems[point_key])

    def remove_line(self, point_key1, point_key2):
        line_key1 = (point_key1, point_key2)
        line_key2 = (point_key2, point_key1)
        if line_key1 in self.lineItems:
            self.mainWindow.view_image_ploygon.scene().removeItem(self.lineItems[line_key1])
        elif line_key2 in self.lineItems:
            self.mainWindow.view_image_ploygon.scene().removeItem(self.lineItems[line_key2])

    def delete_polygon(self, polygon):
        self.mainWindow.view_image_ploygon.scene().removeItem(polygon)

        # Get the points of the polygon
        polygon_points = polygon.polygon().toList()
        # Convert QList<QPointF> to List of tuples
        polygon_points = [(point.x(), point.y()) for point in polygon_points]

        # Remove points and lines from the scene
        for i in range(len(polygon_points)):
            self.remove_point(polygon_points[i])
            self.remove_line(polygon_points[i-1], polygon_points[i])

        # Convert polygon_points to list of QPoints
        polygon_points = [QPointF(point[0], point[1]) for point in polygon_points]

        # Remove the points of the polygon from the list of closed polygons
        if polygon_points in self.mainWindow.view_image_ploygon.scene().closed_polygons:
            self.mainWindow.view_image_ploygon.scene().closed_polygons.remove(polygon_points)

        # Remove points from the list
        self.mainWindow.list_clicked_points.clear()

        # Add remaining polygon points to the list with separator
        for other_polygon_points in self.mainWindow.view_image_ploygon.scene().closed_polygons:
            for point in other_polygon_points:
                self.mainWindow.list_clicked_points.addItem('({:.2f}, {:.2f})'.format(point.x(), point.y()))
            self.mainWindow.list_clicked_points.addItem('...........................')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = event.scenePos()

            # check if click happened on pixmap_item, if not, do nothing
            if self.pixmap_item is not None:
                pixmap_rect = self.pixmap_item.boundingRect()
                if not pixmap_rect.contains(point):
                    return

            # if 3 points are available and close polygon is under mouse, close polygon
            if len(self.points) > 2 and self.close_poly is not None and self.close_poly.isUnderMouse():
                self.add_line(self.points[-1], self.points[0], QColor("red"), 2)
                self.close_poly.setRect(self.points[0].x() - 5, self.points[0].y() - 5, 10, 10)
                self.closed_polygons.append(self.points.copy())
                self.points = []
                self.close_poly = None
                self.mainWindow.list_clicked_points.addItem('...........................')

                # Get the opacity value from the slider and apply it to the polygon
                polygon_opacity = self.mainWindow.slider_polygon_opacity.value() / 100.0
                self.add_polygon(self.closed_polygons[-1], QColor("red"), polygon_opacity)
            
            else:
                # add point to polygon
                self.add_ellipse(point, QColor("red"), 5)
                self.mainWindow.list_clicked_points.addItem('({:.2f}, {:.2f})'.format(point.x(), point.y()))
                if len(self.points) > 0:
                    self.add_line(self.points[-1], point, QColor("red"), 2)
                self.points.append(point)

    def add_ellipse(self, point, color, radius=3):
        # add an ellipse (point) to the scene
        brush = QBrush(color)
        ellipse = QGraphicsEllipseItem(point.x() - radius / 2, point.y() - radius / 2, radius, radius)
        ellipse.setBrush(brush)
        self.addItem(ellipse)
        self.pointItems[(point.x(), point.y())] = ellipse  # store the QGraphicsEllipseItem
        if len(self.points) == 0:
            self.close_poly = ellipse

    def add_line(self, start, end, color, width):
        # add a line to the scene
        pen = QPen(color, width)
        line = QGraphicsLineItem(start.x(), start.y(), end.x(), end.y())
        line.setPen(pen)
        self.addItem(line)
        self.lineItems[((start.x(), start.y()), (end.x(), end.y()))] = line  # store the QGraphicsLineItem

    def add_polygon(self, points, color, opacity):
        # Create a polygon item
        polygon = QPolygonF(points)
        polygon_item = QGraphicsPolygonItem(polygon)

        # Set the color and transparency of the polygon
        brush = QBrush(color)
        polygon_item.setBrush(brush)

        # Create an opacity effect
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(opacity)
        polygon_item.setGraphicsEffect(opacity_effect)

        # Add the polygon to the scene
        self.addItem(polygon_item)

    def mouseMoveEvent(self, event):
        # enlarge closing point when mouse hovers over it
        if len(self.points) > 2 and self.close_poly is not None:
            if self.close_poly.isUnderMouse():
                self.close_poly.setRect(self.points[0].x() - 10, self.points[0].y() - 10, 20, 20)
            else:
                self.close_poly.setRect(self.points[0].x() - 5, self.points[0].y() - 5, 10, 10)

class ImageProcessApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PolyShield Detector")
        self.button_upload_img.clicked.connect(self.select_image)
        self.button_predict.clicked.connect(self.predict_image)
        self.button_clear_lists.clicked.connect(self.clear_lists)

        self.button_upload_img.setCursor(Qt.PointingHandCursor)
        self.button_predict.setCursor(Qt.PointingHandCursor)
        self.button_clear_lists.setCursor(Qt.PointingHandCursor)
        self.slider_polygon_opacity.valueChanged.connect(self.on_slider_changed)
        self.radioButton_points_lines_opacity.toggled.connect(self.on_radio_button_toggled)

        self.radioButton_points_lines_opacity.setChecked(True)

    def on_radio_button_toggled(self):
        # Get the new opacity value from the radioButton
        opacity = 1.0 if self.radioButton_points_lines_opacity.isChecked() else 0.0

        # Update the scene's opacity value
        if self.view_image_ploygon.scene() is not None:
            self.view_image_ploygon.scene().opacity = opacity

            # Apply the new opacity to all lines and points
            items = self.view_image_ploygon.scene().items()
            for item in items:
                if isinstance(item, (QGraphicsLineItem, QGraphicsEllipseItem)):
                    item.setOpacity(opacity)

    def select_image(self):
        # Open file dialog and select image file
        self.list_detected_objects.clear()
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.view_img_path.setText(file_path)
            self.display_image(file_path)

    def create_scene(self, pixmap):
        # Create scene with given pixmap
        scene = CustomGraphicsScene(mainWindow=self)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setPos(0, 0)
        scene.addItem(pixmap_item)
        scene.pixmap_item = pixmap_item
        return scene

    def display_image(self, file_path):
        # Load image from file_path and display
        image = QImage(file_path)
        pixmap = QPixmap.fromImage(image)
        self.view_image_ploygon.setMouseTracking(True)
        old_scene = self.view_image_ploygon.scene()
        new_scene = self.create_scene(pixmap)
        self.view_image_ploygon.setScene(new_scene)
        self.view_image_ploygon.fitInView(self.view_image_ploygon.sceneRect(), Qt.KeepAspectRatio)

        # set dimensions of the new scene
        new_scene_size = new_scene.sceneRect().size()
        self.new_scene_width = new_scene_size.width()
        self.new_scene_height = new_scene_size.height()

        self.current_scene = new_scene

        return old_scene

    def process_nopolygons(self, filename):
        # Handles detection without polygons.
        preds, old_scene = self.process_objects(filename)

        if old_scene is not None:
            self.redraw_polygons(old_scene)

    def predict_image(self):
        # Load image and run object detection
        self.list_detected_objects.clear()
        img_path = self.view_img_path.text()
        filename = os.path.basename(img_path)
        self.filename_base = os.path.splitext(filename)[0]

        # initialize object detection
        self.detector = DetectionPredictor(model_path='models/yolov8x.pt', img_path=img_path, img_output='./output')
        self.detector.predict()

        # process polygons if any
        if self.current_scene.closed_polygons: 
            # process polygons
            self.process_polygons(filename)
        else:
            # process non-polygonal detections
            self.process_nopolygons(filename)

    def process_polygons(self, filename):
        # Handles detection with polygons.
        all_polygons = self.current_scene.closed_polygons
        points_list = []
        for polygon in all_polygons:
            points_list.append([[point.x(), point.y()] for point in polygon])

        preds, old_scene = self.process_objects(filename)
        inside_polygon = []
        for points in points_list:
            inside_polygon.extend(self.filter_objects_inside_polygon(points, preds))
        self.display_inside_polygon(inside_polygon)
        self.redraw_polygons(old_scene)

    def process_objects(self, filename):
        # Load the object detection results from the JSON file and display the recognized objects in the list_detected_objects QListWidget.
        with open(f'records/{self.filename_base}.json') as json_file:
            data = json.load(json_file)

        preds = data['predictions']

        # Count the occurrences of each class label and sort them in ascending order.
        last_elements = [inner_lst[-1] for inner_lst in preds]
        counter = Counter(last_elements)
        sorted_counter = dict(sorted(counter.items()))

        self.list_detected_objects.addItem('List of recognised objects:')
        for key, value in sorted_counter.items():
            self.list_detected_objects.addItem(f'{class_names[int(key)]}: {value} times')
        self.list_detected_objects.addItem('...........................')

        output_img_path = f"./output/{filename}"
        old_scene = self.display_image(output_img_path)

        return preds, old_scene

    def filter_objects_inside_polygon(self, points_list, preds):
        # Filter the objects that are inside the polygon based on their bounding boxes.
        # Calculate the scaled polygon points based on the scene dimensions.
        new_height = self.detector.yolo_resize_height
        new_width = self.detector.yolo_resize_width
        old_height = self.new_scene_height
        old_width = self.new_scene_width

        scaled_polygon_points = [[int(point[0] * new_width / old_width), int(point[1] * new_height / old_height)] for
                                point in points_list]

        polygon = Polygon(scaled_polygon_points)

        inside_polygon = []

        # Check if the intersection area between the polygon and each bounding box is greater than 50% of the bounding box area.
        for obj in preds:
            bbox = box(int(obj[0]), int(obj[1]), int(obj[2]), int(obj[3]))

            if polygon.intersection(bbox).area / bbox.area > 0.5:
                inside_polygon.append(obj)

        # remove duplicates
        inside_polygon = list(set([tuple(i) for i in inside_polygon]))

        return inside_polygon

    def display_inside_polygon(self, inside_polygon):
        # Display the objects that are inside the polygon in the list_detected_objects QListWidget.
        last_elements = [inner_lst[-1] for inner_lst in inside_polygon]
        counter = Counter(last_elements)
        sorted_counter = dict(sorted(counter.items()))

        self.list_detected_objects.addItem('List of objects inside the polygons:')
        for key, value in sorted_counter.items():
            self.list_detected_objects.addItem(f'{class_names[int(key)]}: {value} times')

    def redraw_polygons(self, old_scene):
        # Redraws the polygons from an old scene to the current scene.
        polygons = old_scene.closed_polygons.copy()

        for polygon in polygons:
            for i in range(len(polygon)):
                self.view_image_ploygon.scene().add_ellipse(polygon[i], QColor("red"), 5)
                if i > 0:
                    self.view_image_ploygon.scene().add_line(polygon[i - 1], polygon[i], QColor("red"), 2)
            self.view_image_ploygon.scene().add_line(polygon[-1], polygon[0], QColor("red"), 2)

        self.view_image_ploygon.scene().closed_polygons = polygons

        # Re-draw and fill the polygons after processing
        for polygon in self.current_scene.closed_polygons:
            opacity = self.slider_polygon_opacity.value() / 100.0
            self.current_scene.add_polygon(polygon, QColor("red"), opacity)

    def clear_lists(self):
        # clear polygon and reset scene
        self.view_image_ploygon.scene().clear()
        self.list_clicked_points.clear()
        self.view_image_ploygon.scene().closed_polygons = []
        self.view_image_ploygon.scene().points = []
        self.view_image_ploygon.scene().close_poly = None
        self.display_image(self.view_img_path.text())

    def on_slider_changed(self):
        # Get the new opacity value from the slider
        opacity = self.slider_polygon_opacity.value() / 100.0

        # Apply the new opacity to all polygons
        for polygon_item in self.view_image_ploygon.scene().items():
            if isinstance(polygon_item, QGraphicsPolygonItem):
                polygon_item.graphicsEffect().setOpacity(opacity)


if __name__ == "__main__":
    # Check if the "output" folder exists, and create it if it doesn't
    if not os.path.exists('output'):
        os.makedirs('output')

    # Check if the "records" folder exists, and create it if it doesn't
    if not os.path.exists('records'):
        os.makedirs('records')

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/icon.png"))
    window = ImageProcessApp()
    window.show()

    sys.exit(app.exec())

# 點擊顯示的種類
# 限制辨識的種類
# 添加右列分頁，顯示種類與辨識顯示按鈕
# 把yolov8圖放在圖片中最上面，僅次點位，可使用一個按鈕控制透明度
# json加上old size(label_img_size), new side(predict_img_size), label points, objects data inside polygons, objects data outside polygons