import os

# Project Root Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Test Path to IMU Raw Data File
IMU_PATH = os.path.join(ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')

# # Path to IMU Raw Data File
# IMU_PATH = "path to raw data file"

# # Create UDEV rules symlink for /dev/video-cam
# f = open("/etc/udev/rules.d/avvs-cam.rules", "w")
# f.write('KERNEL=="video[0-9]*", SUBSYSTEM=="video4linux", SUBSYSTEMS=="usb", ATTRS{idVendor}=="05a9", ATTRS{idProduct}=="4519", SYMLINK+="video-cam"')
# f.close()

# # Path to camera device ID using udev rules' symlink
# CAPTURE_DEVICE = "/dev/video-cam"

# Name of the capture device, which should be viewable from `lsusb`
DEVICE_NAME = "Logitech, Inc. Webcam C920"

## How often a frame is processed (seconds)
FRAME_INTERVAL = 1

## Device's viewport angle in degrees
VIEWPORT_ANGLE = 78

## Output detected objects and bounding boxes
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
USE_PITCH = False
USE_YAW = False

# ================ END Image Manipulation Configs ================ #
