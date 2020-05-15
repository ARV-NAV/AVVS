import unittest
from object_detection import detect_and_track
from object_detection import CentroidTracker as ct
import cv2 as cv


class Test_detect_and_track(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tracker = ct.CentroidTracker()

    # Test that boats can be detected in the image
    def test_detect_in_image(self):
        img = cv.imread("test/mocks/boats_snapshot.png", 1)
        cv.imshow('test',img)
        # Assert 5 boats found
        self.assertEqual(detect_and_track.detect_in_image(img, self.tracker), 5)
