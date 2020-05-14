# AVVS: Autonomous Vessel Vision System

AVVS is a computer vision system developed for the ROSS (Robotic Oceanographic Surface Sampler). The AVVS collects visual data from the environment via a waterproofed front facing camera then detects and categorizes obstacles providing feedback to the navigation system.

## Installation

### Note
*The following installation assumes you have a bash terminal for use on Linux/Mac/Windows*

#### Install Matlab:

*(Note: you must have an active Matlab license and account: [Student account activation.](https://is.oregonstate.edu/service/software/matlab))*

1) Download Matlab runtime R2020a or R2019b from [Mathworks](https://www.mathworks.com/products/compiler/matlab-runtime.html)

2) Unzip the runtime package and install

    * Linux/Mac
        ```bash
        # Example using terminal
        unzip matlab_R2020a_glnxa64.zip
        sudo ./install
        ```
    * Windows

        Unzip the Matlab runtime zip, and run the setup.exe file.

3) Sign in using you Matlab account username, and password

4) Accept the MathWorks Licensing Agreement and click 'Next'

5) Select your active license and click 'Next'

6) Create a login name and click 'Next' *(Note: this name is so Mathworks can Identify specific devices currently logged in)*

7) Select an installation destination folder and click next *(Note: if you select an installation folder other then the default, you may need to add the new location to your PATH variable)*

8) Ensure the following four products are selected, then click 'Next'

    * MATLAB

9) Decide if you want to send usage data to MathWorks and click 'Next'

10) Click 'Begin Installation'

#### Install Python Dependencies:

1) Locate and save the MATLAB root folder.

    ```bash
    # Example Using Defualt locations
    Linux/Mac: /usr/local/MATLAB/R2020a
    Windows:   /c/Program\ Files\MATLAB\R2020a
    ```

2) Navigate to the venv.sh file.

    Update the *matlab_root_dir* variable to use the path saved from (1)

    Update the *absolute_path_to_venv* variable to use the absolute path for the virtual environment.

        This path has not been created yet, and it will be installed where the repository was cloned. (E.g. git cloned to /test/AVVS; venv will be in /test/AVVS/venv)
        For Windows the path must be in Windows format (i.e. "C:\test\AVVS\venv" instead of "/c/test/AVVS/venv").

3) Make sure virtualenv is installed

    ```bash
   $ pip install virtualenv
    ```

4) Update the venv.sh file variable to use python3

    ```bash
   python=python3 
   ```

5) In your bash terminal. Navigate to the AVVS directory, update the venv.sh to be an executable and run the venv.sh file

    ```bash
   # Example command
   $ pwd
   /test/AVVS
   $ chmod +x ./venv.sh
   $ ./venv.sh
    ```

   Note: matlab is only installed into the virtual environment and is not available outside of it.
   To use matlab outside the virtual environment follow this [guide](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).

6) Navigate to the main.py file.

    Update the shebang to include the path to your virtual environment.
    ```bash

   Linux/Mac : #!./venv/bin/python
   Windows   : #!./venv/Scripts/python
    ```

## Configuration

1) Open config.py in the project root directory with your chosen editor

2) Comment out the IMU_PATH variable that points 'IMU_timestamped_test_data.bin' and un-comment the line ``` IMU_PATH="path to raw data file"```, replacing ```"path to raw data file"``` with the absolute path to the live IMU data file.


3) Replace the value of CAPTURE_DEVICE with the video capture id of the camera used for collecting visual data. Use the command 'ls /dev/video*' from the terminal to discover available video capture devices on the system. To chose the correct device, unplug the video camera to be used from the system, list available video capture devices, then plug the USB camera in and run the command again. Use the new device.

```bash
# example
ls /dev/video*

# output ...bash
/dev/video0
/dev/video1
```

## Usage
Starting the AVVS will begin reading the data file pointed to by IMU_PATH config variable and output positional data on detected objects to stdout. If the DRAW_TO_SCREEN configuration variable is set, a processed image will be generated containing a orientation corrected view port with bounding boxes around detected objects.

```bash
# Run the AVVS
./main.py

# Run the AVVS output to a file
./main.py > file.txt
```

To run another file on its own you must use the path to the virtual environment's python script.

```bash
Linux/Mac: ./venv/bin/python
Windows  : ./venv/Scripts/python

# Example Usage
Linux/Mac: ../venv/bin/python image_transformation.py
Windows  : ../venv/Scripts/python image_transformation.py
```

## Testing

- Run all Tests command:

    ```
    Linux/Mac: ./venv/bin/python -m unittest
    Windows  : ./venv/Scripts/python -m unittest
    ```
## IMU Field Description

Unit descriptions and field name for IMU data.

```
    'units': { 
        'attitude': { 
            'compensated_angular_rate': { 
                'X': 'rads/sec',
                'Y': 'rads/sec',
                'Z': 'rads/sec',
                'valid': '1=valid, 0=invalid'
            },
            'gps_timestamp': { 
                'time_of_week': 'seconds',
                'valid': '1=valid, 0=invalid',
                'week_number': 'n/a'
            },
            'heading_update_source_state': { 
                'heading': 'radians',
                'heading_1_sigma_uncertainty': 'radians',
                'source': '0=no source, 1=Magnetometer, 4=External',
                'valid': '1=valid, 0=invalid'
            },
            'linear_acceleration': { 
                'X': 'm/sec^2',
                'Y': 'm/sec^2',
                'Z': 'm/sec^2',
                'valid': '1=valid, 0=invalid'
            },
            'orientation_euler_angles': { 
                'pitch': 'radians',
                'roll': 'radians',
                'valid': '1=valid, 0=invalid',
                'yaw': 'radians'
            }
        }
    }
```
