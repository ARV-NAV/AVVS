""" Script to do object detection with deep neural network.
    The DNN is loaded, and colors and labels are defined before
    an infinite loop runs to detect objects in a video feed input.
"""
# ================ Built-in Imports ================ #

import time

# ================ Third Party Imports ================ #

import cv2
import numpy as np
from object_detection import ObjData

# ================ Authorship ================ #

__author__ = "Donald Max Harkins"
__contributors__ = ["Donald Max Harkins"]

# ================ Initialization ================ #

# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow(
    'object_detection/ssd_inception_v2_smd_2019_01_29/frozen_inference_graph.pb',
    'object_detection/ssd_inception_v2_smd_2019_01_29/graph.pbtxt')

# Set up a list of class labels. There's a tensorflow method,
# but in this case I'm just creating a list since there's only
# 10 classes... Refactor later. See ./ssd_inc...1_29/labels.pbtxt
# Upon further experimentation, this list seems to be out of order
LABELS = ['Ferry',
          'Buoy',
          'Vessel/ship',
          'Speed boat',
          'Boat',
          'Kayak',
          'Sail boat',
          'Swimming person',
          'Flying bird/plane',
          'Other',
          '????',
          'dock?']

# initialize a list of colors to represent each possible class label
np.random.seed(37)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
                           dtype="uint8")


# Define function to process Tensorflow network output
def process_dnn_output(network_output, rows, cols):
    # Loop on the outputs
    rects = []
    for detection in network_output[0, 0]:
        score = float(detection[2])
        if score > 0.5:
            # Subtract 1 since LABEL list is 0 indexed while DNN output is 1 indexed
            obj_id = int(detection[1]) - 1
            # print("Found a " + LABELS[obj_id] + " with confidence " + str(detection[2]))
            left = int(detection[3] * cols)
            top = int(detection[4] * rows)
            right = int(detection[5] * cols)
            bottom = int(detection[6] * rows)
            # Size is a measure of the bounding box area
            size = (detection[6] - detection[4]) * (detection[5] - detection[3])
            data = ObjData.ObjData((left, bottom, right, top),
                                   # datetime.datetime.now().strftime("%H:%M:%S.%f"),
                                   time.time(),
                                   LABELS[obj_id],
                                   detection[2],
                                   int(COLORS[obj_id][0]),
                                   size)
            # centroid tracker takes format smallerX, smallerY, largerX, largerY
            # and a data object/tuple/structure/etc.
            rects.append([left, bottom, right, top, data])
    return rects


def detect_in_image(img, ct):
    """Detect and track objects in image

    @param: img (np array): 3D array representing pixels in image
    @param: cd (CentroidTracker): tracker to persistently track found objects

    """
    h, w = img.shape[:2]

    # Use the given image as input, which needs to be blob(s).
    # Originally, parameters for blob were
    # blobFromImage(img,size=(300,300), swapRB=True, crop=True)
    # This seems to work better
    tensorflowNet.setInput(
        cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)),
                              swapRB=True, crop=True))

    # Runs a forward pass to compute the net output
    network_output = tensorflowNet.forward()

    # Get list of objects from tensorflow network output
    rows, cols = img.shape[:2]
    rects = process_dnn_output(network_output, rows, cols)

    # Now, update the centroid tracker with the newly found bounding boxes
    tracked_objs = ct.update(rects)

    return len(rects)
