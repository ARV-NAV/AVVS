import os

class DefaultEnv():
    ROOT_DIR=os.path.dirname(os.path.abspath(__file__))

class TestEnv(DefaultEnv):
    IMU_PATH=os.path.join(DefaultEnv.ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')

class ProdEnv(DefaultEnv):
    IMU_PATH="Nothing yet"

def getEnv(env):
    if env == 'prod':
        return ProdEnv
    elif env == 'test':
        return TestEnv
    else:
        return DefaultEnv