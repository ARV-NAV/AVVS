# Object to store data associated with each obstacle detected in each frame

import cv2 as cv2

class objData():
    def __init__(self, rect, timestamp, label, confidence, color):
        self.rect = rect
        self.timestamp = timestamp
        self.label = label
        self.confidence = confidence
        self.color = color

    def drawData(self, img):
         #draw a coloured rectangle around object.
         # rectangle did not play nice with numpy array, hence manual casting
         # Draw some text too
         (startX, startY, endX, endY) = self.rect
         text = "{} | {:.4f} | {}".format(self.label, self.confidence, self.timestamp)
         cv2.putText(img, text, (startX, startY - 5),
             cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.color, 2)
         cv2.rectangle(img, (startX, startY), (endX, endY), self.color, thickness=2)
