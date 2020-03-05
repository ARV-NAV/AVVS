# Starting code by Jean Vitor, available at https://jeanvitor.com/tensorflow-object-detecion-opencv/
import cv2
import numpy as np

# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow(
        'ssd_inception_v2_smd_2019_01_29/frozen_inference_graph.pb'
        , 'ssd_inception_v2_smd_2019_01_29/graph.pbtxt')

# Set up a list of class labels. There's a tensorflow method,
# but in this case I'm just creating a list since there's only
# 10 classes... Refactor later
labels = ['Ferry',
          'Buoy',
          'Vessel/ship',
          'Speed boat',
          'Boat',
          'Kayak',
          'Sail boat',
          'Swimming person',
          'Flying bird/plane'
          'Other']

# initialize a list of colors to represent each possible class label
np.random.seed(38)
colors = np.random.randint(0, 255, size=(len(labels), 3),
	dtype="uint8")

# Input image
img = cv2.imread('img.png')
rows, cols, channels = img.shape

# Use the given image as input, which needs to be blob(s).
tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

# Runs a forward pass to compute the net output
networkOutput = tensorflowNet.forward()

# Loop on the outputs
for detection in networkOutput[0,0]:

    score = float(detection[2])
    if score > 0.2:
        objID = int(detection[1])+1
        print("Found a " + labels[objID])
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows

        #draw a coloured rectangle around object.
        # rectangle did not play nice with numpy array, hence manual casting
        theColor = (int(colors[objID][0]), int(colors[objID][1]), int(colors[objID][2]))
        # Draw some text too
        text = "{}: {:.4f}".format(labels[objID], detection[2])
        cv2.putText(img, text, (int(left), int(top) - 5),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, theColor, 2)
        cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), theColor, thickness=2)

# Show the image with a rectagle surrounding the detected objects
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()
