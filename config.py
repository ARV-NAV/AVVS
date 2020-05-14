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

# Device's viewport angle in degrees
VIEWPORT_ANGLE = 78

# Output detected objects and bounding boxes
DRAW_TO_SCREEN = True

# Verbose output
VERBOSE = False
