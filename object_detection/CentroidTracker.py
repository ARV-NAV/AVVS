""" Centroid tracker based on code by Adrian Rosebrock
    (Avaliable:  https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/)
    * Takes a list of rectangles at each time step, and
    matches them by dynamically minimizing the euclidian
    distance between center points from one frame to another.
    * Also stores information about each detected object over
    time by keeping a dictionary of lists of data objects.
    * Contains a draw method which displays all objects
    being tracked on an image.
"""

# ================ Built-in Imports ================ #
from collections import OrderedDict

# ================ Third Party Imports ================ #

from scipy.spatial import distance as dist
import numpy as np

# ================ User Imports ================ #

from object_detection import TrackedObject


# ================ Class defenition ================ #
class CentroidTracker:
    def __init__(self, max_disappeared=20):
        # initialize the next unique object ID along with two ordered
        # dictionaries used to keep track of mapping a given object
        # ID to its centroid and number of consecutive frames it has
        # been marked as "disappeared", respectively
        self.nextObjectID = 0
        self.objects = OrderedDict()

        # store the number of maximum consecutive frames a given
        # object is allowed to be marked as "disappeared" until we
        # need to deregister the object from tracking
        self.maxDisappeared = max_disappeared

    def draw_objects(self, img):
        # loop over the tracked objects and display the centroid
        for (objID, obj) in self.objects.items():
            obj.draw_object(objID, img)

    def register(self, centroid, data_obj):
        # when registering an object we use the next available object
        # ID to store the centroid
        self.objects[self.nextObjectID] = TrackedObject.TrackedObject(centroid, data_obj)
        self.nextObjectID += 1

    def deregister(self, object_id):
        # to deregister an object ID we delete the object ID from
        # both of our respective dictionaries
        del self.objects[object_id]

    # Parameter newObjs is a list of rectangle lists [startX, startY, endX, endY]
    def update(self, new_objs):
        # check to see if the list of input bounding box rectangles
        # is empty
        if len(new_objs) == 0:
            # loop over any existing tracked objects and mark them
            # as disappeared
            for object_id in list(self.objects.keys()):
                self.objects[object_id].update(disappeared=True)

                # if we have reached a maximum number of consecutive
                # frames where a given object has been marked as
                # missing, deregister it
                if self.objects[object_id].disappeared > self.maxDisappeared:
                    self.deregister(object_id)

            # return early as there are no centroids or tracking info
            # to update
            return self.objects

        # initialize an array of input centroids for the current frame
        input_centroids = np.zeros((len(new_objs), 2), dtype="int")
        input_data = []
        # loop over the bounding box rectangles
        for (i, (startX, startY, endX, endY, dataObj)) in enumerate(new_objs):
            # use the bounding box coordinates to derive the centroid
            c_x = int((startX + endX) / 2.0)
            c_y = int((startY + endY) / 2.0)
            input_centroids[i] = (c_x, c_y)
            input_data.append(dataObj)

        # if we are currently not tracking any objects take the input
        # centroids and register each of them
        if len(self.objects) == 0:
            for i in range(0, len(input_centroids)):
                self.register(input_centroids[i], input_data[i])

        # otherwise, we are currently tracking objects so we need to
        # try to match the input centroids to existing object
        # centroids
        else:
            # grab the set of object IDs and corresponding centroids
            object_ids = list(self.objects.keys())
            object_centroids = [o.centroid for o in self.objects.values()]

            # compute the distance between each pair of object
            # centroids and input centroids, respectively -- our
            # goal will be to match an input centroid to an existing
            # object centroid
            d = dist.cdist(np.array(object_centroids), input_centroids)

            # in order to perform this matching we must (1) find the
            # smallest value in each row and then (2) sort the row
            # indexes based on their minimum values so that the row
            # with the smallest value as at the *front* of the index
            # list
            rows = d.min(axis=1).argsort()

            # next, we perform a similar process on the columns by
            # finding the smallest value in each column and then
            # sorting using the previously computed row index list
            cols = d.argmin(axis=1)[rows]

            # in order to determine if we need to update, register,
            # or deregister an object we need to keep track of which
            # of the rows and column indexes we have already examined
            used_rows = set()
            used_cols = set()

            # loop over the combination of the (row, column) index
            # tuples
            for (row, col) in zip(rows, cols):
                # if we have already examined either the row or
                # column value before, ignore it
                # val
                if row in used_rows or col in used_cols:
                    continue

                # otherwise, grab the object ID for the current row,
                # set its new centroid, and reset the disappeared
                # counter
                object_id = object_ids[row]
                self.objects[object_id].update(centroid=input_centroids[col],
                                               data=input_data[col])

                # indicate that we have examined each of the row and
                # column indexes, respectively
                used_rows.add(row)
                used_cols.add(col)

            # compute both the row and column index we have NOT yet
            # examined
            unused_rows = set(range(0, d.shape[0])).difference(used_rows)
            unused_cols = set(range(0, d.shape[1])).difference(used_cols)

            # in the event that the number of object centroids is
            # equal or greater than the number of input centroids
            # we need to check and see if some of these objects have
            # potentially disappeared
            if d.shape[0] >= d.shape[1]:
                # loop over the unused row indexes
                for row in unused_rows:
                    # grab the object ID for the corresponding row
                    # index and increment the disappeared counter
                    object_id = object_ids[row]
                    self.objects[object_id].update(disappeared=True)

                    # check to see if the number of consecutive
                    # frames the object has been marked "disappeared"
                    # for warrants deregistering the object
                    if self.objects[object_id].disappeared > self.maxDisappeared:
                        self.deregister(object_id)

            # otherwise, if the number of input centroids is greater
            # than the number of existing object centroids we need to
            # register each new input centroid as a trackable object
            else:
                for col in unused_cols:
                    self.register(input_centroids[col], input_data[col])

        # return the set of trackable objects
        return self.objects
