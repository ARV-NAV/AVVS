import unittest
import os
from config import ROOT_DIR
from classes.Imu import Imu
from test.mocks.parsed_imu_data import imu_data_mock, imu_last_data_mock
from numpy.testing import assert_allclose

MOCK_IMU_PATH = os.path.join(ROOT_DIR, 'test/mocks/IMU_timestamped_test_data.bin')


class Test_IMU(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imu = Imu(MOCK_IMU_PATH)

    def test_parse_imu_data(self):
        data = self.imu.parse_imu_data()
        self.assertIsNotNone(data)
        assert_allclose(data['heading'], imu_data_mock['heading'],
                           err_msg="Heading", verbose=True, atol=1e-6)
        assert_allclose(data['pitch'], imu_data_mock['pitch'],
                           err_msg="pitch", verbose=True, atol=1e-6)
        assert_allclose(data['yaw'], imu_data_mock['yaw'],
                           err_msg="yaw", verbose=True, atol=1e-6)
        assert_allclose(data['roll'], imu_data_mock['roll'],
                           err_msg="roll", verbose=True, atol=1e-6)
        assert_allclose(data['nuc_time'], imu_data_mock['nuc_time'],
                           err_msg="nuc_time", verbose=True, atol=1e-6)

    def test_get_last_orientation(self):
        data = self.imu.get_last_orientation()
        self.assertIsNotNone(data)
        assert_allclose(data['heading'], imu_last_data_mock['heading'],
                           err_msg="Heading", verbose=True, atol=1e-6)
        assert_allclose(data['pitch'], imu_last_data_mock['pitch'],
                           err_msg="pitch", verbose=True, atol=1e-6)
        assert_allclose(data['yaw'], imu_last_data_mock['yaw'],
                           err_msg="yaw", verbose=True, atol=1e-6)
        assert_allclose(data['roll'], imu_last_data_mock['roll'],
                           err_msg="roll", verbose=True, atol=1e-6)
        assert_allclose(data['nuc_time'], imu_last_data_mock['nuc_time'],
                           err_msg="nuc_time", verbose=True, atol=1e-6)