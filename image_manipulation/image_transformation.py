"""Provides Image Manipulation Module

Functions provided in this module alter the input images
to then pass to object detection algorithms
"""
# ================ Built-in Imports ================

from math import cos, sin
from typing import Tuple

# ================ Third Party Imports ================

from numpy import ndarray, matmul, array
from cv2 import imread, warpPerspective, INTER_LANCZOS4

# ================ Authorship ================

__author__ = "Gregory Sanchez"


def get_transformation_matrix(orientation: dict, img_szie: Tuple[float, float]) -> ndarray:
    """Get Transformation Matrix

    Creates the matrix transformation for the image based
    off the orientation data.
    This was taken from https://stackoverflow.com/a/37279632
    """
    roll = orientation["pitch"].item(0)
    pitch = orientation["yaw"].item(0)
    yaw = orientation["roll"].item(0)
    dx, dy, dz = 0, 0, 1

    cx, cy = img_szie  # principal point that is usually at the image center

    focal_mm = 3.67  # This is specific for a Logitech c920 Camera (TODO: make sure this is correct)
    sensor_width_mm = 4.8  # This is specific for a Logitech c920 Camera

    # focal_mm = 26  # This is specific for a Samsung Galaxy S8 Rear Camera
    # sensor_width_mm = 7.06  # This is specific for a Samsung Galaxy S8 Rear Camera

    f = (focal_mm / sensor_width_mm) * (cx * 2)  # focal length expressed in pixel units

    # Camera Calibration Intrinsics Matrix
    a2 = array([
        [f, 0, cx, 0],
        [0, f, cy, 0],
        [0, 0, 1,  0]
    ], dtype=float)

    # Inverted Camera Calibration Intrinsics Matrix
    a1 = array([
        [1/f,   0,   -cx/f],
        [0,     1/f, -cy/f],
        [0,     0,   0],
        [0,     0,   1]
    ], dtype=float)

    # Rotation matrices around the X, Y, and Z axis
    rx = array([
        [1,     0,          0,          0],
        [0,     cos(roll),  -sin(roll), 0],
        [0,     sin(roll),  -cos(roll), 0],
        [0,     0,          0,          1]
    ], dtype=float)

    ry = array([
        [cos(pitch),    0, sin(pitch),  0],
        [0,             1, 0,           0],
        [-sin(pitch),   0, cos(pitch),  0],
        [0,             0, 0,           1]
    ], dtype=float)

    rz = array([
        [cos(yaw), -sin(yaw), 0, 0],
        [sin(yaw),  cos(yaw), 0, 0],
        [0,         0,        1, 0],
        [0,         0,        0, 1]
    ], dtype=float)

    # Translation matrix
    t = array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ], dtype=float)

    # Compose rotation matrix with RX, RY, RZ (RZ * RY * RX)
    # r = matmul(matmul(rz, ry), rx)
    r = matmul(matmul(rz, rx), ry)

    # Final transformation matrix (A2 * (T * (R * A1))
    h = matmul(a2, matmul(t, matmul(r, a1)))

    return h


def rotate_image(img: ndarray, orientation: dict) -> ndarray:
    """Rotate Image

    @param: img_path (str): path to the image to rotate
    @param: orientation (dict): orientation data of the vessel

    @return: numpy array with the (un)altered image
    """
    # img = imread(img_path, 0)
    cols, rows, colors = img.shape

    t = get_transformation_matrix(orientation, (rows/2, cols/2))
    dst = warpPerspective(img, t, (rows, cols), flags=INTER_LANCZOS4)

    return dst


if __name__ == "__main__":
    from cv2 import imshow, waitKey, destroyAllWindows, imwrite

    test_data = {
        "pitch": 0,
        "yaw": 0,
        "roll": 1.0472,  # 60 degrees
    }

    # The following image was captured with a Samsung Galaxy S8
    # new_img = rotate_image('./images/img_30_2.jpg', test_data)

    # The following image was captured with a Logitech c920 Camera
    new_img = rotate_image('./logitech_camera/data/frame129.jpg', test_data)

    imwrite("saved_img.jpg", new_img)

    imshow('img', new_img)
    waitKey(0)
    destroyAllWindows()
