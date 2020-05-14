""" Python Unit Test for Image Tranformation
"""

# ================ Built-in Imports ================ #

import unittest
from os import path

# ================ Third Party Imports ================ #

import cv2
from imutils import rotate
from skimage.metrics import structural_similarity

# ================ User Imports ================ #

from config import ROOT_DIR
from image_manipulation import image_transformation
from test.mocks.parsed_imu_data import imu_last_valid_data_mock_roll_60_deg

# ================ Authorship ================ #

__author__ = "Gregory Sanchez"


IMG_PATH = path.join(ROOT_DIR, 'image_manipulation/logitech_camera/data/frame129.jpg')


class TestImageTransformation(unittest.TestCase):

    def test_img_rotate(self):
        """Test Image Rotate
            Ensures that the rotation from image_transformation is correct"""
        img = cv2.imread(IMG_PATH)

        # Get the image_transformation and expected image
        actual = image_transformation.rotate_image(img, imu_last_valid_data_mock_roll_60_deg)
        expected = rotate(img, -60)

        gray_a = cv2.cvtColor(actual, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(expected, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two images
        (score, _) = structural_similarity(gray_a, gray_b, full=True)
        print("SSIM: {0}".format(score))

        self.assertGreaterEqual(score, 0.99)
