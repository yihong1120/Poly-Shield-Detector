# User Guide

This user guide will walk you through the steps to install PySide6 library in a macOS virtual environment using Anaconda, and resolve the issue of not being able to invoke Qt-Designer in the terminal. Please follow the steps below:

## Step 1: Install PySide6

On macOS, follow these steps using Anaconda virtual environment:

1. Open the terminal.

2. Activate the desired virtual environment. For example, use the following command to activate a virtual environment named **GUI_YOLOv8**:

```shell
conda activate GUI_YOLOv8
```

3. Install PySide6 using the following command:

```shell
pip install pyside6
```

## Step 2: Modify the bashrc file

1. In the terminal, use the following command to open the **bashrc** file for editing:

```shell
vim ~/.bashrc
```

2. Add the following content to the end of the **bashrc** file. Note that **GUI_YOLOv8** is the name of your virtual environment, so modify it according to your actual environment name:

```shell
export PATH=$PATH:/System/Volumes/Data/opt/anaconda3/envs/GUI_YOLOv8/bin/pyside6-designer
export DYLD_LIBRARY_PATH=/usr/local/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/config-3.11-darwin:$DYLD_LIBRARY_PATH
export PYSIDE_DESIGNER_PLUGINS=/opt/anaconda3/envs/GUI_YOLOv8/lib/python3.11/site-packages/PySide6/plugins/designer
```

3. Save and exit the **bashrc** editor.

## Step 3: Update environment variables

1. In the terminal, enter the following command to apply the updated **bashrc** file:

```shell
source ~/.bashrc
```

## Step 4: Launch Qt-Designer

1. In the terminal, enter the following command to launch Qt-Designer:

```shell
pyside6-designer
```

## Step 5: Convert .ui files to .py files

1. Assuming you have a GUI interface file named **ImageProcess.ui**, you can use the following command to convert it to **imageprocess_ui.py**:

```shell
pyside6-uic ImageProcess.ui -o imageprocess_ui.py
```

The above steps will guide you in installing PySide6 in a macOS virtual environment using Anaconda and resolving the issue with Qt-Designer. If you have any further questions, feel free to contact us.