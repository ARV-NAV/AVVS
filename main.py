""" Description of the main entry point
"""

# ================ Built-in Imports ================ #

import os
import argparse

# ================ Third Party Imports ================ #

import cv2 as cv

# ================ User Imports ================ #

import enviroment
from classes.Imu import Imu
from image_manipulation import image_transformation
from object_detection import detect_and_track
from object_detection import CentroidTracker

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez", "Donald 'Max' Harkens", "Tobias Hodges"]

# ================ Global Variables ================ #

# ================ Functions ================ #


def getArgs():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", help="Set enviroment: 'prod', or 'dev' (default)")
    return vars(ap.parse_args())


# ================ Main ================ #

if __name__ == "__main__":

    # Parse Command Line Arguments
    args = getArgs()

    # get configuration
    config = enviroment.getEnv(args['env'])

    # Component initilization
    imu = Imu(config.IMU_PATH)

    # Video Frame Streaming
    cap = cv.VideoCapture(config.CAPTURE_DEVICE)

    # Set up video writer
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (1200, 675))

    # Set up object tracker
    tracker = CentroidTracker.CentroidTracker()


    while True:
        # Press Q on keyboard to  exit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        # get image
        ret, img = cap.read()
        if not ret:
            break

        # get attitude if valid image
        attitude = imu.get_last_valid_orientation()

        # Transform image
        transformed_image = image_transformation.rotate_image(img, attitude)

        # detect and classify object
        detect_and_track.detect_in_image(transformed_image, tracker)

        # display on system
        if (config.DRAW_TO_SCREEN):
            # Draw the objects being tracked
            tracker.drawObjects(transformed_image)
            cv.imshow('Tracked Objects', transformed_image)

        # calculate pos

        # output pos

    # Clean up
    cap.release()
    out.release()
    cv.destroyAllWindows()
