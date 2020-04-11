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
            self.assertEqual(len(tracker.objects), len(tracker.objectData))

        # Deregister Objects
        for i in range(0, numObjects):
            tracker.deregister(i)
            self.assertEqual(len(tracker.objects), len(tracker.objectData))
            self.assertEqual(len(tracker.objects), numObjects - (i+1))
            self.assertEqual(tracker.nextObjectID, numObjects)

        self.assertFalse(any(tracker.objects))
