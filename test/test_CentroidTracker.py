import unittest
from object_detection.CentroidTracker import CentroidTracker


class Test_CentroidTracker(unittest.TestCase):

    #@classmethod
    # def setUpClass(cls):
    #    cls.tracker = CentroidTracker()

    def test_register_deregister(self):
        tracker = CentroidTracker()
        self.assertEqual(len(tracker.objects), tracker.nextObjectID)

        testCentroid = (0,0)
        testData = None
        numObjects = 10

        # Register 10 objects
        for i in range(1, numObjects+1):
            tracker.register(testCentroid, testData)
            self.assertEqual(tracker.nextObjectID, i)
            self.assertEqual(len(tracker.objects), i)

        # Deregister Objects
        for i in range(0, numObjects):
            tracker.deregister(i)
            self.assertEqual(len(tracker.objects), numObjects - (i+1))
            self.assertEqual(tracker.nextObjectID, numObjects)

        self.assertFalse(any(tracker.objects))

    def test_update(self):
        # initialize tracker where object can dissapear for at most 1 frame
        tracker = CentroidTracker(maxDisappeared=1)

        # initialize list of new objects to track
        objsToAdd = []
        for i in range(0,10):
            objsToAdd.append((i, i, i+1, i+1, None))

        # update empty CentroidTracker
        tracker.update(objsToAdd)

        # Assert all objects were added to empty tracker
        self.assertEqual(len(tracker.objects), len(objsToAdd))

        # Update with an empty list
        tracker.update([])

        # Assert the disappeared count is 1 for all objects
        for i in range(len(objsToAdd)):
            self.assertEqual(tracker.objects[i].disappeared, 1)

        # Update with empty list again
        tracker.update([])

        # Assert all objects removed from tracker (since max disappeared exceeded)
        self.assertEqual(len(tracker.objects), 0)
