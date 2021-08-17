# Custom Module Tutorial

## Introduction

3D Slicer's plug-in mechanism allow application developers to add a new features and customize 3D Slicer for their specific clinical applications. Those new features are called "Modules." Modules may be packaged and provided as "Extensions," which can be distributed to users through [Extension Manager](https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html).

There are three mechanisms that are used to develop modules:
- '''Command-line interface (CLI) module:''' A command-line program that can be called from 3D Slicer. 3D Slicer parses a configuration file bundled with a CLI module, and automatically generates a GUI interface for the user to give pass parameters to the CLI module. Many image processing modules are implemented as CLI modules.
- '''Loadable module:''' A Plug-in module written in C++, the same language used for the foundation of 3D Slicer (including [VTK](https://vtk.org/) and [ITK](https://itk.org/). The loadable module can access most of the native C++ API in 3D Slicer, it offers the highest flexibility and performance to the developers among the three mechanisms. However, it required more effort than the other approaches as the development of a loadable module geenrally involves more codings and compilation.
- '''Scripted module:''' A plug-in module written in Python. Scripted module has become very popular among the Slicer developers in recent years, because of its simplicity, flexibility, and portability.

In this tutorial, we will develop a Scripted module.


## Notes on Python Interface in 3D Slicer..

Scripted modules use Python interface in 3D Slicer. Users can directory interact with the Python interface through "Python Interactor," which is a convinient way to test part of their codes interactively. [Script Repository](https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html) provides various code snippets to demonstrate how to call Slicer API through the Python interface.


## Goal of Our Custom Module - "Proximity Warning"

As an example CAS application, we will build a "Proximity Warning" module. The module monitors incoming tool tracking data, and warns if the tool tip comes too close to a given target point.

The user will select the following parameters:
- '''Linear transform node:''' a node to store the tracking data are imported from external tracking system.
- '''Markups fiducial node:''' a node that defines a target point.
- '''Distance:''' A threshold distance that defines the "proximity" from the target point.

The threshold distance is visualized as a sphere in the 3D space. When the tip comes into the proximity range (i.e., the distance between the tool tip and the target point becomes shorter than the given threshold distance), the module changes the color of the sphere from blue to red.


## Step-by-Step Instruction

### Step 1: Create an Extension

First, we create an extension.

1. From the "Modules" menu, choose "Developer Tools" -> "Extension Wizard"
2. Click "Create Extension."
3. A dialog box should appear on the screen. Type in the following information:
  1. Name: "CASTutorial"
  2. Type: "default"
  3. Destination: Your working directory (folder) (will be refered to as "the working directory" in the following steps)
4. Click "OK"
5. Another dialog box should appear. You may edit the category, description, and contributor. Click "OK" to close.

### Step 2: Create a "sekeleton" code for a module.

Within the Extension created in Step 1, we add a new module.

1. Under the "Extension Editor" in the "Extenssion Wizard," click "Add Module to Extension."
2. A dialog box should appear. Type the name of the module ("ProximityWarning") and choose "scripted" (default) as the type.
3. Click "OK" to close the dialog box.
4. Another dialog box shows up and asks if you want to load the module now. Click "Yes."

After 1-4, a "skeleton" python code is generated under the working directory. The directory structure should look like:

~~~~
CASTutorial
├── CASTutorial.png
├── CMakeLists.txt
└── ProximityWarning
    ├── CMakeLists.txt
    ├── ProximityWarning.py
    ├── Resources
    │   ├── Icons
    │   │   └── ProximityWarning.png
    │   └── UI
    │       └── ProximityWarning.ui
    ├── Testing
    │   ├── CMakeLists.txt
    │   └── Python
    │       └── CMakeLists.txt
    └── __pycache__
        └── ProximityWarning.cpython-36.pyc
~~~~

The main python code is "ProximityWarning/ProximityWarning.py".


### Step 3: Edit GUI

Edit the GUI using Qt Designer. Please refer to [Tutorial on Qt Designer](https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner) for detail.

In this tutorial, we edit ProximityWarning/Resources/UI/ProximityWarning.ui using Qt Designer. Open the file with Qt Designer and make the following changes:

- Input volume label
 - Change the name from "Input volume:" to "Input Tracker:"
 - Change the type from "vtkMRMLLinearTransformNode" to "vtkMRMLScalarVolumeNode"

- Slider 
 - Change the label from "threshold:" to "Distance (mm):"
 - Change the name from "imageThresholdSliderWidget" to "distanceSliderWidget"

- Add new qMRMLNodeComboBox
 - Name: "fiducialSelector"
 - Node type: "vtkMRMLMarkupsFiducialNode"
 - Label: Fiducial

In some environments (especially in macOS), 3D Slicer cannot launch Qt Designer using the '--designer' option. You can find some discussion on [Slicer Forum](https://discourse.slicer.org/t/edit-ui-raies-designer-cannot-be-opened-because-of-a-problem/13176). If it does not solve the issue, please download the .ui file from [the tutorial page](https://github.com/tokjun/SlicerForCASTutorial/tree/main/ProximityWarning/Resources/UI) and copy it into the Resources/UI directory to replace the old one generated by the Extension Wizard.


# Step 4: Edit the source code

Next, we edit the main source code (ProximityWarning/ProximityWarning.py). The source code 

First, import the numpy library in the code. Ad the following line after at the begining of the file:

~~~~
import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

import numpy       # <---- Here!
~~~~

In the ProximityWarningWidget class, we will use two class-wide variables to keep the node ID and tag (which is an identifier of the event observer). At the end of the constructor ( __init__() function), add the following two lines:

~~~~
  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

    self.inputNodeID = False    # <---- Here!
    self.inputTag = False       # <---- Here!
~~~~

In Qt, each GUI widget emits a "signal" when there is any updates (e.g., mouse click, button release, value change, etc). To capture the signal and define the behaviour of the program upon the emission of a signal, the developer must define a special call back function called "slot" and connect it with the GUI widget that emits the signal.

Our module must react to two GUI events:
1. Change of the input node (the linear transform node that receives the tracking data)
2. Change of the distance value

To handle the change of the input node, we define the following function in the ProximityWarningWidget class:

~~~~
  def setInputNode(self, caller=None, event=None):
    
    newNode = self.ui.inputSelector.currentNode()
    if self.inputTag: # If an observer for the old node exists
      oldNode = slicer.mrmlScene.GetNodeByID(self.inputNodeID)
      if oldNode:
        oldNode.RemoveObserver(self.inputTag)
        
    if newNode:
      self.inputTag = newNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, self.onInputModified)
      self.inputNodeID = newNode.GetID()
    else:
      self.inputTag = None
      self.inputNodeID = None
~~~~

This function takes a new linear transform node from the inputSelector widget, and register an 'observer' function, which observes the node and process the data when the node is updated. This is achieved by calling AddObserver(). The actual observer function (self.onInputModified()) will be defined later.

The change of the distance value is handled by onDistanceUpdated() function. We insert the following definition under the ProximityWarningWidget class:

~~~~
  def onDistanceUpdated(self, caller=None, event=None):
    inputNode = self.ui.inputSelector.currentNode()
    fidNode = self.ui.fiducialSelector.currentNode()
    distance = self.ui.distanceSliderWidget.value
    self.logic.proximityCheck(inputNode, fidNode, distance)
~~~~       

The function called in the last line (self.logic.proximityCheck()) defines how to check the distance between the current tool tip (inputNode) and the target point (fidNode), and determines whether the tool tip is within the defined range. The function will be defined later in this section.

Next, we define the observer function, onInputModified() (see above). This function is called when the inputNode is updated (i.e., the tracking data is updated by the external software). Again, we call the same self.logic.proximityCheck() function as we did in onDistanceUpdated(). We add the following function under the ProximityWarningWidget class:

~~~~
  @vtk.calldata_type(vtk.VTK_OBJECT)
  def onInputModified(self, caller, eventId):
    inputNode = self.ui.inputSelector.currentNode()    
    fidNode = self.ui.fiducialSelector.currentNode()
    distance = self.ui.distanceSliderWidget.value
    self.logic.proximityCheck(inputNode, fidNode, distance)
~~~~

We implement proximityCheck() as a member function of the logic class (ProximityWarningLogic). Before adding proximityCheck(), we define three class member variables in the constructor (__init__(self)):

~~~~
    self.sphere = None
    self.apd = None
    self.modelNodeID = None
~~~~

Then, we define proximityCheck() under the ProximityWarningLogic class as follows:

~~~~
  def proximityCheck(self, transformNode, fidNode, proximityDistance):
  
    print('proximityCheck() distance = ' + str(proximityDistance) + ' mm')
    
    if transformNode == None:
      return

    if fidNode == None:
      return

    # Check if the model node exists; if not create one.
    if self.modelNodeID == None or (slicer.mrmlScene.GetNodeByID(self.modelNodeID) == None):
      modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
      self.modelNodeID = modelNode.GetID()
      
      if self.sphere == None:
        self.sphere = vtk.vtkSphereSource()

      self.sphere.SetThetaResolution(20)
      self.sphere.SetPhiResolution(20)
      self.sphere.SetRadius(0)
      self.sphere.SetCenter([0.0, 0.0, 0.0])
      self.sphere.Update()
      
      if self.apd == None:
        self.apd = vtk.vtkAppendPolyData()
        self.apd.AddInputConnection(self.sphere.GetOutputPort())
        
      self.apd.Update()
      modelNode.SetAndObservePolyData(self.apd.GetOutput())
      modelNode.Modified()

    modelNode = slicer.mrmlScene.GetNodeByID(self.modelNodeID)
    nPoints = fidNode.GetNumberOfFiducials()
    
    if nPoints > 0:
      pos = [0.0]*3
      fidNode.GetNthFiducialPosition(0, pos)

      self.sphere.SetRadius(proximityDistance)
      self.sphere.SetCenter(pos)
      self.sphere.Update()
      self.apd.Update()
      modelNode.Modified()
      
      dispNode = modelNode.GetDisplayNode()
      if dispNode == None:
        dispNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelDisplayNode')
        modelNode.SetAndObserveDisplayNodeID(dispNode.GetID())

      # Calculate the distance between the fiducial point and the tracking point
      matrix = vtk.vtkMatrix4x4()
      transformNode.GetMatrixTransformToParent(matrix)
      x = matrix.GetElement(0, 3)
      y = matrix.GetElement(1, 3)
      z = matrix.GetElement(2, 3)
      
      t = numpy.array([x, y, z])
      f = numpy.array(pos)  # The coordinates of the fiducial point

      d = numpy.linalg.norm(t-f)

      # Set color of the sphere
      prevState = dispNode.StartModify()
      
      if d < proximityDistance:
        dispNode.SetColor([1.0, 0.0, 0.0]) # Red if the distance is < proximityDistance
      else:
        dispNode.SetColor([0.0, 0.0, 1.0]) # Blue if the distance is >= proximityDistance
        
      dispNode.SetOpacity(0.5)
      dispNode.SliceIntersectionVisibilityOn()
      dispNode.Visibility2DOn()
      dispNode.SetSliceDisplayModeToIntersection()
      dispNode.EndModify(prevState)
~~~~  







