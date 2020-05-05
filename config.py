import os

# Project Root Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Test Path to IMU Raw Data File
IMU_PATH = os.path.join(ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')

# Path to IMU Raw Data File
# IMU_PATH = "path to raw data file"

# Path to video file or camera device ID
CAPTURE_DEVICE = 'MVI_1610_VIS_cut.avi'

# Device's viewport angle in degrees
VIEWPORT_ANGLE = 78

# Output detected objects and bounding boxes
DRAW_TO_SCREEN = True

VERBOSE = False

# ================ Image Manipulation Configs ================ #

# Focal length and sensor width of the camera in use (in mm)
#          Logitech c920; Focal Length: 3.67; Sensor Width: 4.8
#          Samsung Galaxy s8 Rear Camera; Focal Length: 26; Sensor Width: 7.06
CAM_FOCAL_LENGTH = 3.67
CAM_SENSOR_WIDTH = 4.8

# Signals to determine which axis to include for the image manipulation
USE_ROLL = True
USE_PITCH = True
USE_YAW = False

# ================ END Image Manipulation Configs ================ #
