# AVVS: Autonomus Vessle Vission System

AVVS is a computer vision system developed for the ROSS (Robotic Oceanagraphic Surface Sampler). The AVVS collects visual data from the enviroment via a waterproofed front facing camera then detects and catagorizes obsticals providing feedback to the navigation system.

## Installation

### Windows

Blah, blah, blah!!!

### Linux

#### Install OpenCV:

```bash
pip3 install opencv-python
```

#### Install Matlab:

*(Note: you must have an active Matlab license and account: [Student account activation.](https://is.oregonstate.edu/service/software/matlab))*

1) Download matlab runtime R2020a or R2019b from [Mathworks](https://www.mathworks.com/products/compiler/matlab-runtime.html)

2) Unzip the runtime package and install

    ```bash
    # Example using terminal
    unzip matlab_R2020a_glnxa64.zip
    sudo ./install
    ```
3) Sign in using you matlab account username, and password

4) Accept the MathWorks Licensing Agreement and click 'Next'

5) Select your active license and click 'Next'

6) Create a login name and click 'Next' *(Note: this name is so Mathworks can Identify specific devices currently logged in)*

7) Select an installation destination folder and click next *(Note: if you select an installation folder other then the default, you may need to add the new location to your PATH variable)*

8) Ensure the following four products are selected, then click 'Next'

    * MATLAB
    * Simulink
    * Statistics and Machine Learning Toolbox
    * Symbolic Math Toolbox

9) Decide if you want to send usage data to MathWorks and click 'Next'

10) Click 'Begin Installation'

#### Install Matlab Engine for Python:

1) Navigate to your MATLAB root folder *(Note: generally, '/usr/local/MATLAB/R2020a' if you used the default location)*

2) Enter the following command to install engine

    ```bash
    sudo python extern/engines/python/setup.py install
    ```

## Configuration

1) Open config.py in the project root directory with your chosen editor

2) Comment out the IMU_PATH variable that points 'IMU_timestamped_test_data.bin' and un-comment the line ``` IMU_PATH="path to raw data file"```, replacing ```"path to raw data file"``` with the absolute path to the live IMU data file.

3) Replace the value of CAPTURE_DEVICE with the divece id of the camera used for collecting visual data. Use the command 'lsusb' from the terminal to discover your webcam's id which you can enter into the CAPTURE_DEVICE variable.
```bash
# example
lsusb

# output ...
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 004: ID 138a:0097 Validity Sensors, Inc. 
Bus 001 Device 003: ID 04ca:7067 Lite-On Technology Corp. Integrated Camera
Bus 001 Device 002: ID 8087:0a2b Intel Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

```

## Usage
Starting the AVVS will begin reading the data file pointed to by IMU_PATH config variable and output positional data on detected objects to stdout. If the DRAW_TO_SCREEN configuration variable is set, a processed image will be generated containing a orientation corrected view port with bounding boxes around detected objects.

```bash 
# Run the AVVS 
python main.py

# Run the AVVS output to a file
python main.py > file.txt

```

## Testing
- Run all Tests command: ```python -m unittest```