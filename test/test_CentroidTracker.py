import unittest
from object_detection.CentroidTracker import CentroidTracker


class TestCentroidTracker(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #    cls.tracker = CentroidTracker()

    def test_register_deregister(self):
        tracker = CentroidTracker()
        self.assertEqual(len(tracker.objects), tracker.nextObjectID)

        test_centroid = (0, 0)
        test_data = None
        num_objects = 10

        # Register 10 objects
        for i in range(1, num_objects + 1):
            tracker.register(test_centroid, test_data)
            self.assertEqual(tracker.nextObjectID, i)
            self.assertEqual(len(tracker.objects), i)

        # Deregister Objects
        for i in range(0, num_objects):
            tracker.deregister(i)
            self.assertEqual(len(tracker.objects), num_objects - (i + 1))
            self.assertEqual(tracker.nextObjectID, num_objects)

        self.assertFalse(any(tracker.objects))

    def test_update(self):
        # initialize tracker where object can dissapear for at most 1 frame
        tracker = CentroidTracker(max_disappeared=1)

        # initialize list of new objects to track
        objs_to_add = []
        for i in range(0, 10):
            objs_to_add.append((i, i, i + 1, i + 1, None))

        # update empty CentroidTracker
        tracker.update(objs_to_add)

        # Assert all objects were added to empty tracker
        self.assertEqual(len(tracker.objects), len(objs_to_add))

        # Update with an empty list
        tracker.update([])

        # Assert the disappeared count is 1 for all objects
        for i in range(len(objs_to_add)):
            self.assertEqual(tracker.objects[i].disappeared, 1)

        # Update with empty list again
        tracker.update([])

        # Assert all objects removed from tracker (since max disappeared exceeded)
        self.assertEqual(len(tracker.objects), 0)
