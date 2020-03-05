"""Provides Image Manipulation Module

Functions provided in this module alter the input images
to then pass to object detection algorithms
"""
# ================ Built-in Imports ================

from sys import stderr
from math import cos, sin
from typing import Tuple

# ================ Third Party Imports ================

from numpy import ndarray, matmul
from cv2 import imread, getRotationMatrix2D, warpAffine, warpPerspective, INTER_LANCZOS4

# ================ Authorship ================

__author__ = "Gregory Sanchez"


def get_transformation_matrix(orientation: dict, img_szie: Tuple[float, float]) -> ndarray:
    """Get Transformation Matrix

    Creates the matrix transformation for the image based
    off the orientation data.
    This was taken from https://stackoverflow.com/a/37279632
    """
    roll = orientation["roll"]
    pitch = orientation["pitch"]
    yaw = orientation["yaw"]
    dx, dy, dz = 0, 0, 1

    f = 1  # focal length expressed in pixel units (TODO: Figure out)

    cx, cy = img_szie  # principal point that is usually at the image center (TODO: Figure out)

    # Camera Calibration Intrinsics Matrix
    a2 = [
        [f, 0, cx, 0],
        [0, f, cy, 0],
        [0, 0, 1,  0]
    ]

    # Inverted Camera Calibration Intrinsics Matrix
    a1 = [
        [1/f,   0,   -cx/f],
        [0,     1/f, -cy/f],
        [0,     0,   0],
        [0,     0,   1]
    ]

    # Rotation matrices around the X, Y, and Z axis
    r_x = [
        [1,     0,          0,          0],
        [0,     cos(roll),  -sin(roll), 0],
        [0,     sin(roll),  -cos(roll), 0],
        [0,     0,          0,          1]
    ]

    r_y = [
        [cos(pitch),    0, sin(pitch),  0],
        [0,             1, 0,           0],
        [-sin(pitch),   0, cos(pitch),  0],
        [0,             0, 0,           1]
    ]

    r_z = [
        [cos(yaw), -sin(yaw), 0, 0],
        [sin(yaw),  cos(yaw), 0, 0],
        [0,         0,        1, 0],
        [0,         0,        0, 1]
    ]

    # Translation matrix
    t = [
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ]

    # Compose rotation matrix with RX, RY, RZ (RZ * RY * RX)
    r = matmul(matmul(r_z, r_y), r_x)

    # Final transformation matrix (A2 * (T * (R * A1))
    h = matmul(a2, matmul(t, matmul(r, a1)))

    return h


def rotate_image(img_path: str, orientation: dict) -> ndarray:
    """Rotate Image

    @param: img_path (str): path to the image to rotate
    @param: orientation (dict): orientation data of the vessel

    @return: numpy array with the (un)altered image
    """
    img = imread(img_path, 0)
    rows, cols = img.shape

    t = get_transformation_matrix(orientation, (rows/2, cols/2))
    # import pdb; pdb.set_trace()
    print(t)
    dst = warpPerspective(img, t, (rows, cols), flags=INTER_LANCZOS4)

    # try:
    #     roll = orientation["roll"]
    #     rot_matrix = getRotationMatrix2D((cols/2, rows/2), roll, 1)
    #     dst = warpAffine(img, rot_matrix, (cols, rows))
    # except KeyError as err:
    #     print("Key Error: unknown key {0}".format(err), file=stderr)
    #     dst = img

    return dst


if __name__ == "__main__":
    from cv2 import imshow, waitKey, destroyAllWindows

    test_data = {
        "pitch": 0.03037297911942005,
        "yaw": 0.03037297911942005,
        "roll": 0.03037297911942005
    }

    new_img = rotate_image('./images/img_downscale_30.jpg', test_data)

    imshow('img', new_img)
    waitKey(0)
    destroyAllWindows()
