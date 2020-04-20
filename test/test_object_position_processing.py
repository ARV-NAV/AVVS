import unittest
from classes.object_position_processing import calculate_angle


class Test_object_position_processing(unittest.TestCase):

    def test_get_object_angle(self):
        width = 1920
        height = 1080
        viewport_angle = 45
        #Tests case for object pixels that are on the optical sensor centerline
        object_x = 960
        object_y = 200
        self.assertTrue(calculate_angle(width, height, viewport_angle, object_x, object_y) == 0)

        #Test for case where the object pixels are greater than the centerline
        object_x = 1560
        object_y = 700
        self.assertTrue(calculate_angle(width, height, viewport_angle, object_x, object_y) ==  12.256530990813975)

        #Test for case where the object pixels are less than the centerline
        object_x = 500
        object_y = 700
        self.assertTrue(calculate_angle(width, height, viewport_angle, object_x, object_y) == 9.396673759624047)
