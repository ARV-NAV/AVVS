""" Description of the main entry point
"""

# ================ Built-in Imports ================ #

import os
import argparse

# ================ Third Party Imports ================ #

import cv2 as cv

# ================ User Imports ================ #

from classes.Imu import Imu
from image_manipulation import image_transformation
import enviroment

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez", "Donald 'Max' Harkens", "Tobias Hodges"]

# ================ Global Variables ================ #

# ================ Functions ================ #

def getArgs():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", help="Set enviroment: 'prod', 'test', or 'dev' (default)")
    return vars(ap.parse_args())


# ================ Main ================ #

if __name__ == "__main__":
    
    # Parse Command Line Arguments
    args = getArgs();

    # get configuration
    config = enviroment.getEnv(args['env'])

    # Component initilization
    imu = Imu(config.IMU_PATH)

    while True:
        # get image
        
        # get attitude if valid image
        attitude = imu.get_last_valid_orientation()

        # Transform image

        # detect and classify object

        # track objects

        # calculate pos

        # output pos


        



