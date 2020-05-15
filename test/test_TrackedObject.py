import unittest
from object_detection.TrackedObject import TrackedObject
from object_detection.ObjData import ObjData


class TestTrackedObject(unittest.TestCase):

    def test_update_new_apperance(self):
        center = (1, 1)
        size = 0.2
        time = 1

        obj = TrackedObject(center, ObjData((0, 0, 2, 2), time, "Boat", 0.99, 255, size))

        # Assert that upon initialization, tracker obj has a centroid but no doubling_time
        # and has not been marked as disappeared
        self.assertEqual(obj.centroid, center)
        self.assertEqual(obj.size_increase, None)
        self.assertEqual(obj.disappeared, 0)

        new_center = (2, 2)
        new_size = 0.4
        new_time = 2

        obj.update(centroid=new_center, data=ObjData((0, 0, 4, 4), new_time, "Boat", 0.99, 255, new_size))

        # Assert that the center has been updated, our boat has a positive value for halving time
        # since the angular size is increasing
        self.assertEqual(obj.centroid, new_center)
        self.assertGreater(obj.size_increase, 0)
        self.assertEqual(obj.disappeared, 0)

    def test_update_disappeared_true(self):
        center = (1, 1)
        size = 0.2
        time = 1

        obj = TrackedObject(center, ObjData((0, 0, 2, 2), time, "Boat", 0.99, 255, size))

        obj.update(disappeared=True)

        # Assert nothing has changed since initialization except for a disappearance is marked
        self.assertEqual(obj.centroid, center)
        self.assertEqual(obj.disappeared, 1)
        self.assertEqual(len(obj.data), 1)

    def test_update_no_params(self):
        center = (1, 1)
        size = 0.2
        time = 1

        obj = TrackedObject(center, ObjData((0, 0, 2, 2), time, "Boat", 0.99, 255, size))

        # Record old state
        old_centroid = obj.centroid
        old_data = obj.data
        old_disappeared = obj.disappeared
        old_halving_time = obj.size_increase

        obj.update()

        # Assert no state changes when no parameters are passed to update method
        self.assertEqual(obj.centroid, old_centroid)
        self.assertEqual(obj.data, old_data)
        self.assertEqual(obj.disappeared, old_disappeared)
        self.assertEqual(obj.size_increase, old_halving_time)
