"""
============================
Dummy Tracking Server
============================

A simple OpenIGTLink server program that sends dummy tracking data to the client.

"""

import pyigtl  # pylint: disable=import-error
from math import cos, sin, pi
from time import sleep
import numpy as np

server = pyigtl.OpenIGTLinkServer(port=18944, local_server=True)

timestep = 0

while True:

    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue

    timestep += 1

    # Generate dummy transform
    matrix = np.eye(4)
    
    matrix[0, 3] = sin(timestep * 0.05) * 50.0
    matrix[1, 3] = sin(timestep * 0.03) * 50.0
    matrix[2, 3] = sin(timestep * 0.08) * 50.0
    
    rotation_angle_rad = timestep * 0.5 * pi / 180.0
    matrix[1, 1] = cos(rotation_angle_rad)
    matrix[2, 1] = -sin(rotation_angle_rad)
    matrix[1, 2] = sin(rotation_angle_rad)
    matrix[2, 2] = cos(rotation_angle_rad)
    transform_message = pyigtl.TransformMessage(matrix, device_name="Tracking")

    # Send messages
    server.send_message(transform_message)

    # Do not flood the message queue,
    # but allow a little time for background network transfer
    sleep(0.01)


