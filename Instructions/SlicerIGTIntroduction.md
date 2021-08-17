# SlicerIGT Introductory Tutorial

## Introduction

[SlicerIGT](http://www.slicerigt.org/) provides a set of features that are commonly used for image-guided therapy (IGT) applications. Those features include, but are not limited to:

- Fiducial registration (point-to-point, point-to-model)
- Pivot calibration
- Breach warning
- Create model elements
- Image reformatting

SlicerIGT is often used with [PLUS Toolkit](https://plustoolkit.github.io/), an independent software package designed for data acquisition, preprocessing, calibration, and real-time streaming of imaging, position tracking, and other sensor data. PLUS Toolkit can communicate with 3D Slicer for advanced visualization and user interaction.

This tutorial briefly overviews how SlicerIGT works. [The official SlicerIGT website](http://www.slicerigt.org/) offers a variety of tutorials that allow the developers to learn how to use 3D Slicer, SlicerIGT, and PLUS Toolkit to build an IGT system for their clinical applications. 

## Step-by-Step Instruction

### Step 1: Install SlicerIGT

To install both extensions:

1. Open Extension Manager from "View" -> "Extension Manager."
2. In the Extension Manager dialog window, choose the "Install Extensions" tab.
3. Find "SlicerIGT" and click "INSTALL."
4. Find "SlicerIGT" and click "INSTALL."
5. After the extensions are downloaded, restart the Slicer by clicking the "Restart" button at the right-bottom corner of the Extension Manager dialog window.

If the extensions are successfully installed, you should find them from the module menu. Please refer to [3D Slicer User Guide](https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html) for further instruction on Slicer Extension.


### Step 2: Set up a dummy tracking server

Please follow Step 2-4 in [Tool Tracking Tutorial](ToolTracking.md).

The following steps assume that the tracking data is being imported into 3D Slicer.


### Step 3: Visualize the tracking data as a model

In the previous tutorial ([Tool Tracking Tutorial](ToolTracking.md)), we simply used the SlicerOpenIGTLink extension's function to visualize the tracking data as a needle in the 3D viewer. However, users can use any polygon model to show the current tool position.

1. From the "Modules" menu, choose "IGT" -> "CreateModels."
2. Under the "Needle model" section, click the "Create needle" button. (You may change the Length, Radius, and Tip radius parameters before clicking the button)
3. From the "Modules" menu, open "Data."
4. Open the "Transform hierarchy" tab. You could see "Tracking" under the "Scene," if tracking data is properly imported.
5. You could also see "NeedleModel" under the "Scene," if the needle model has been properly created.
6. (Optional) If you click "Show MRML ID's," you can confirm the types of nodes in the scene. The "Tracking" and "NeedleModel" nodes should have an ID that begins with "vtkMRMLLinearTransformNode?" and "vtkMRMLModelNode?". '?' is a number automatically assigned by the scene and varies depending on the nodes that have already been in the scene.
7. Drug and drop the "NeedleModel" node under the "Tracking" node. The "NeedleModel" node should become a child branch of the "Tracking" node, meaning that the transform for the "Tracking" node is now being applied to the "NeedleModel" node.
8. You could see the needle model is moving in the 3D viewer.

You can use other models (e.g., cube, sphere, etc) instead of the needle model.


### Step 4: Reformat a volume image

Volume "reslicing" or "reformatting" is a technique to cut a volumetric image (e.g., CT, MRI) along with a 2D plane and visualize the section. Many surgical navigation software packages provide this feature to show the anatomical structures along with the tracked tool. Volume reformatting has also been one of the core features in 3D Slicer, and it is named after this feature.

1. From the "Modules" menu, choose "Welcome to Slicer."
2. Click the "Download Sample Data" button.
3. Click "MRHead" (the first image shown under the "BuiltIn" section). The 3D Slicer starts downloading the image. The progress will appear in the status bar at the bottom of the 3D Slicer window.
4. Once the image is downloaded, it should appear in the 2D viewers. Note that the original images are acquired in the sagittal plane (which is shown in the yellow viewer), and the other two planes (i.e., red and green) are reformatted images.
5. To show the image in the 3D viewer, click the "Pin" icon at the top-left corner of each 2D viewer (the left end of the red, green, or yellow bar at the top of the viewer). The image selector bar appears below the red, green, or yellow bar. Click the "Eye" button (the third button from the left) to show the corresponding slice in the 3D viewer.
6. From the "Modules" menu, choose "IGT" -> "Volume Reslice Driver."
7. From the "Driver" menus in the red, green, and yellow control panels, choose "Tracking."
8. From the "Mode" menus in the red control panel, choose "Axial."
9. From the "Mode" menus in the green control panel, choose "Coronal."
10. From the "Mode" menus in the yellow control panel, choose "Sagittal."
11. The slices in the 3D viewer should follow the tip of the moving needle.
12. From the "Mode" menus in the red control panel, choose "Inplane."
13. From the "Mode" menus in the green control panel, choose "Inplane90."
14. From the "Mode" menus in the yellow control panel, choose "Transverse."
15. The slices in the 3D viewer should be kept aligned with the moving needle.
16. (Optional) Under the "Advanced options," click the "Show advanced options" check box. The "Rotation" slider appears in each control panel.
17. (Optional) Move the "Rotation" slider to rotate the plane about the needle axis.


### Step 5: Stop Tracking

1. From the "Modules" menu, choose "IGT" -> "OpenIGTLinkIF."
2. Under the "Connectors" section, choose the connector (it should already be selected, if there is only one connector in the scene).
3. Check off the "Active" check box.
4. Go to the terminal where the tracking server is running, and press Ctrl-C to stop the python script.








