import cv2
import numpy as np
from object_detection.CentroidTracker import CentroidTracker
from object_detection.ObjData import ObjData
import datetime


# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow(
        'object_detection/ssd_inception_v2_smd_2019_01_29/frozen_inference_graph.pb'
        , 'object_detection/ssd_inception_v2_smd_2019_01_29/graph.pbtxt')


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
def process_DNN_output(networkOutput, rows, cols):
    # Loop on the outputs
    rects = []
    for detection in networkOutput[0,0]:
        score = float(detection[2])
        if score > 0.5:
            # Subtract 1 since LABEL list is 0 indexed while DNN output is 1 indexed
            objID = int(detection[1])-1
            # print("Found a " + LABELS[objID] + " with confidence " + str(detection[2]))
            left = int(detection[3] * cols)
            top = int(detection[4] * rows)
            right = int(detection[5] * cols)
            bottom = int(detection[6] * rows)
            data = ObjData((left, bottom, right, top),
                           datetime.datetime.now().strftime("%H:%M:%S.%f"),
                           LABELS[objID],
                           detection[2],
                           int(COLORS[objID][0]))
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
        cv2.dnn.blobFromImage(cv2.resize(img,(300,300)),
        swapRB=True, crop=True))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()

    # Get list of objects from tensorflow network output
    rows, cols = img.shape[:2]
    rects = process_DNN_output(networkOutput, rows, cols)

    # Now, update the centroid tracker with the newly found bounding boxes
    (objects, data) = ct.update(rects)
