# AVVS: Autonomus Vessle Vission System

AVVS is a computer vision system developed for the ROSS (Robotic Oceanagraphic Surface Sampler). The AVVS collects visual data from the enviroment via a waterproofed front facing camera then detects and catagorizes obsticals providing feedback to the navigation system.

## Installation

### Windows

Blah, blah, blah!!!

### Linux

Install OpenCV:

```bash
pip3 install opencv-python
```

Install Matlab:

*(Note: you muse have a active Matlab licence and accout)*

1) Download matlab runtime R2020a from [Mathworks](https://www.mathworks.com/products/compiler/matlab-runtime.html)

2) Unzip the runtime package and install

    ```bash
    # Example using terminal
    unzip matlab_R2020a_glnxa64.zip
    sudo ./install
    ```
3) Sign in using you matlab account username, and password

4) Accept the MathWorks Licenseing Agreement and click 'Next'

5) Select your active license and click 'Next'

6) Create a login name and click 'Next' *(Note: this name is so Mathworks can Identify specific devices currently logged in)*

7) Select an installation destination folder and click next *(Note: if you select an instalation folder other then the default, you may need to add the new location to you PATH variable)*

8) Ensure the following four products are selected, then click 'Next'

    * MATLAB
    * Simulink
    * Statistics and Machine Learning Toolbox
    * Symbolic Math Toolbox

9) Decide if you want to send usage data to MathWorks and click 'Next'

10) Click 'Begin Installation'



## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Testing
- Run all Tests command: ```python -m unittest```

## License
TODO