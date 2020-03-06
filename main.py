""" Description of the main entry point
    """


# ================ Built-in Imports ================ #
import argparse
import os

# ================ Third Party Imports ================ #
from classes.Imu import Imu

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez", "Donald 'Max' Harkens", "Tobias Hodges"]

# ================ Global Variables ================ #

# ================ Functions ================ #

# ================ Main ================ #

if __name__ == "__main__":
    
    # Parse Command Line Arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("--imu", required=True,
	    help="path to imu data file")
    ap.add_argument("-t", action="store_true",
	    help="run tests if set")
    args = vars(ap.parse_args())

    # If test flag set
    if (args['t']):
        imu = Imu("./test/mocks/IMU_timestamped_test_data.bin")
        valid = imu.get_last_valid_orientation()
        print("IMU Test Resultes:")
        print(valid)
    else: 
        imu = Imu(args['imu'])