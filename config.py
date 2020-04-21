import os

## Project Root Directory
ROOT_DIR=os.path.dirname(os.path.abspath(__file__))

## Test Path to IMU Raw Data File
IMU_PATH=os.path.join(ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')

## Path to IMU Raw Data File
# IMU_PATH="path to raw data file"

# Path to video file or camera device ID
CAPTURE_DEVICE = 'MVI_1610_VIS_cut.avi'

# Device's viewport angle in degrees
VIEWPORT_ANGLE = 78

# Output detected objects and bounding boxes
DRAW_TO_SCREEN = True

VERBOSE = False;