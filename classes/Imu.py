"""Python wrapper to parse the IMU binary data
    Module to read binary data outputted from the IMU and convert it to a usable python object
    Uses a predefined MatLab parser to parse through the binary data.
    The parsed data is converted into a dict containing all of the IMU data."""

# ================ Built-in Imports ================ #

from time import time
import config
import os

# ================ Third Party Imports ================ #

import matlab.engine as m_engine
import numpy as np

# REMOVE ME!!!
# import pprint

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez"]

# ================ Class defenition ================ #

# REMOVE ME!!!
# pp = pprint.PrettyPrinter(indent=2)

class Imu:

    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        start_time = time()
        print("Initilizing IMU...")
        self.eng = m_engine.start_matlab()
        print("Initilization Complete. Time elapsed: {0}s".format(time() - start_time) )
        self.eng.addpath(os.path.join(config.ROOT_DIR, '3rd_party_scripts'))

    def get_last_orientation(self) -> dict:
        """Get Last Orientation
            Grabs the last set of binary values from the binary file.
            Opens and reads the file through MatLab itself to then send it through the parser
            Documentation of the DsFileReader: https://www.mathworks.com/help/matlab/ref/matlab.io.datastore.dsfilereader-class.html
        @return: dict: data containing the orientations
        """

        start_time = time()
        orientation = self.eng.parse_imu(self.filepath, self.eng.logical(1))

        # REMOVE ME!!!
        # pp.pprint(orientation)

        new_dict = {'heading':np.asarray(orientation['GNSS']['velocity_north_east_down_frame']['heading']),
            'pitch':np.asarray(orientation['IMU']['cf_euler_angles']['pitch']),
            'roll':np.asarray(orientation['IMU']['cf_euler_angles']['roll']),
            'yaw':np.asarray(orientation['IMU']['cf_euler_angles']['yaw']),
            # 'valid_heading':np.asarray(orientation['IMU']['cf_euler_angles']['valid_flags']),
            'valid_orientation':1,
            'nuc_time':np.asarray(orientation['IMU']['nuc_time'])
        }
        return new_dict
        

    def get_last_valid_orientation(self) -> dict:
        
        """Get Last Valid Orientation
        Gets the last valid set of orientation data from the orientation dictionary
        @return: dict: data containing the last valid orientations data
        """

        orientation_data = self.get_last_orientation();

        # i = 0
        # while (i < 10):
        #     if(orientation_data['valid_heading'][0][9 - i] == 1 and orientation_data['valid_orientation'][0][9 - i] == 1):
        #         valid_data = {'heading':np.asarray(orientation_data['heading'][0][i]),
        #                     'pitch':np.asarray(orientation_data['pitch'][0][i]),
        #                     'roll':np.asarray(orientation_data['roll'][0][i]),
        #                     'yaw':np.asarray(orientation_data['yaw'][0][i]),
        #                     'nuc_time':np.asarray(orientation_data['nuc_time'][0][i]) }
        #         return valid_data
        #     else:
        #         i+=1

        # REMOVE ME
        # print(len(orientation_data['heading'][0]))
        # print(len(orientation_data['pitch'][0]))
        # print(len(orientation_data['roll'][0]))
        # print(len(orientation_data['yaw'][0]))
        # print(len(orientation_data['nuc_time'][0]))

        valid_data = {'heading':np.asarray(orientation_data['heading'][0][-1]),
                    'pitch':np.asarray(orientation_data['pitch'][0][-1]),
                    'roll':np.asarray(orientation_data['roll'][0][-1]),
                    'yaw':np.asarray(orientation_data['yaw'][0][-1]),
                    'nuc_time':np.asarray(orientation_data['nuc_time'][0][-1]) 
        }

        return valid_data