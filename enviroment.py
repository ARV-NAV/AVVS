import os

class DefaultEnv():
    ROOT_DIR=os.path.dirname(os.path.abspath(__file__))
    IMU_PATH=os.path.join(ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')
    CAPTURE_DEVICE = 0

class ProdEnv(DefaultEnv):
    IMU_PATH="Nothing yet"

def getEnv(env):
    if env == 'prod':
        return ProdEnv
    else:
        return DefaultEnv