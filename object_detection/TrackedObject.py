""" Object to store data used by centroid tracker
    * Stores a list of objData objects to track postition over time
    * Stores a count of all frames where the object has disappeared
    * Stores the most recent centroid for each object
    * Stores and updates doubling time using moving average
"""

# ================ Third Party Imports ================ #

import cv2 as cv2
import math as math

# ================ Authorship ================ #

__author__ = "Donald Max Harkins"
__contributors__ = ["Donald Max Harkins"]

# ================ Class defenition ================ #

# Weight for exponential moving average
ALPHA = 0.15

class TrackedObject():
    def __init__(self, centroid, data):
        self.centroid = centroid
        self.data = [data]
        self.disappeared = 0
        self.size_increase = None                # This is the time untill the distance to the detected object is halved
        self.__exponential_rate_average = None

    # Note that distance is related to angular size where dist = actual width / tan(angular size)
    # Since true size of the object must be known to calculate the distance to an object (given angular size)
    # we opt to simply report the rate of bounding box increase
    def __update_size_increase(self):
        if (len(self.data) > 1):
            t_elapsed = self.data[-1].timestamp - self.data[-2].timestamp
            # Calculate the rate by calculating the time difference and size increase
            size_increase = self.data[-1].size - self.data[-2].size
            rate = size_increase / t_elapsed
            if rate == 0:
                rate = 1e-10

            # Calculate the exponential weighted average if there has already been
            # one rate found, otherwise use the first rate found
            if self.__exponential_rate_average == None:
                self.__exponential_rate_average = rate
            else:
                self.__exponential_rate_average = (1 - ALPHA) * self.__exponential_rate_average + ALPHA * rate

            # Here we set the size_increase public variable as the private exponential average
            # Value is scaled by 10000 to increase human readability
            self.size_increase = 10000*self.__exponential_rate_average

    def update(self, centroid=None, data=None, disappeared=False):
        if disappeared:
            self.disappeared += 1

        if centroid is not None:
            self.centroid = centroid
            self.disappeared = 0

        if data is not None:
            self.data.append(data)
            self.__update_size_increase()

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
