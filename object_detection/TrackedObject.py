""" Object to store data used by centroid tracker
    * Stores a list of objData objects to track postition over time
    * Stores a count of all frames where the object has dissapeared
    * Stores the most recent centroid for each object
    * Stores and updates doubling time using moving average
"""

# ================ Third Party Imports ================ #

import cv2 as cv2

# ================ Authorship ================ #

__author__ = "Donald Max Harkins"
__contributors__ = ["Donald Max Harkins"]

# ================ Class defenition ================ #

class trackedObject():
    def __init__(self, centroid, data):
        self.centroid = centroid
        self.data = [data]
        self.disappeared = 0
        self.doubling_time = None

    def __update_doubling_time(self):
        if (len(self.data) > 1):
            t_elapsed = self.data[-1].timestamp - self.data[-2].timestamp
            size_increase = self.data[-1].size - self.data[-2].size
            rate = size_increase / t_elapsed
            if rate == 0:
                rate = 1e-10
            # Assuming angular size (data.size) continues to increase linearly
            self.doubling_time = self.data[-1].size / rate


    def update(self, centroid=[], data=None, dissapeared=False):
        if dissapeared:
            self.dissapeared += 1

        if len(centroid) > 0:
            self.centroid = centroid
            self.dissapeared = 0

        if data:
            self.data.append(data)
            self.__update_doubling_time()

    def drawObject(self, objID, img):
        text = "ID {}".format(objID)
        cv2.putText(img, text, (self.centroid[0] - 10, self.centroid[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.circle(img, (self.centroid[0], self.centroid[1]), 4, (0, 0, 0), -1)
        # If the most recent data we're storing with the object has a draw function,
        # we call it
        try:
            self.data[-1].drawData(img)
        except AttributeError:
            pass
