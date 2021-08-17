# Tool Tracking Tutorial

## Introduction
[OpenIGTLink](https://openigtlink.org/) is an open-source network communication protocol for image-guided therapy (IGT) applications. It is used as a default network interface for 3D Slicer to exchange data with external software, such as device tracking systems and imaging scanners. The OpenIGTLink interface is provided as an extension package named "SlicerOpenIGTLink."

This tutorial demonstrates how to import tracking data from external software through OpenIGTLink.

## Step-by-Step Instruction

### Step 1: Install SlicerOpenIGTLink

To install the SlicerOpenIGTLink extension:

1. Open Extension Manager from "View" -> "Extension Manager."
2. In the Extension Manager dialog window, choose the "Install Extensions" tab.
3. Find "SlicerOpenIGTLink" and click "INSTALL."
4. After the extension is downloaded, restart the Slicer by clicking the "Restart" button at the right-bottom corner of the Extension Manager dialog window.

If the extensions are successfully installed, you should find them from the module menu. Please refer to [3D Slicer User Guide](https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html) for further instruction on Slicer Extension.


### Step 2: Install pyigtl

Our dummy tracking server is written in Python. To use it, [pyigtl](https://pypi.org/project/pyigtl/) must be installed in your Python environment. From the terminal:

~~~~
pip install pyigtl
~~~~


### Step 3: Run the dummy tracking server

The dummy tracking server is included in this tutorial repository under [TrackingServer](../TrackingServer). Once you place [tracking_server.py](../TrackingServer/tracking_server.py) in your working directory, you can run the program by calling the following command:

~~~~
python tracking_server.py
~~~~

The program opens a TCP/IP socket at port 18944 and waits for a connection from the client (which is 3D Slicer in our case).


### Step 4: Connect to the dummy tracking server from 3D Slicer

To connect 3D Slicer to the dummy tracking server:

1. Open 3D Slicer.
2. Click the "Modules" pull-down menu, and choose "IGT"->"OpenIGTLinkIF".
3. Under the "Connectors" section, click "+" to create a connector.
4. You don't need to change the properties (Type=Client, Hostname='localhost', Port='18944') unless you are running the server on a different machine, or have changed the port number of the server.
5. Click the "Active" check box next for "Status."

If 3D Slicer is successfully connected to the dummy tracking server, the "Status" column in the list should become "ON."

### Step 5: Visualize the incoming tracking data

To visualize the tracking data in the 3D viewer:

1. Go to "I/O Configuration" section in the OpenIGTLinkIF extension.
2. Expand "IGTLConnector" by clicking the triangle on the left. It should show "IN" and "OUT" under "IGTLConnector."
3. If the tracking data are being received from the server, "IN" can be further expanded.
4. Under "IN," you could find "Tracking" with an "eye" icon.
5. Click the "eye" icon. A model of the tracked tool should appear and move randomly in the 3D viewer.












