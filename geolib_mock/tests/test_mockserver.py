# pylint: disable=R0904,C0103
""":class:`geolib_mock.MockServer` tests.

"""
import unittest2
import os

import geolib_mock


class TestMockServer(unittest2.TestCase):
    """:class:`geolib_mock.MockServer` test cases.
    """
    @classmethod
    def setUp(cls):
        cls._mock = geolib_mock.MockServer()

    def test_init(self):
        """Initialise a geolib_mock.NITF object.
        """
        msg = 'Object is not a geolib_mock.MockServer'
        self.assertIsInstance(self._mock, geolib_mock.MockServer, msg)

    def test_start_stop(self):
        """Start/stop the Accumulo mock server.
        """
        conf = os.path.join('geolib_mock',
                            'tests',
                            'files',
                            'proxy.properties')
        self._mock.properties_file = conf
        self._mock.start()
        msg = 'Mock server instance should be ACTIVE'
        self.assertTrue(self._mock.is_active, msg)

        self._mock.stop()
        msg = 'Mock server instance should be INACTIVE'
        self.assertFalse(self._mock.is_active, msg)

    @classmethod
    def tearDown(cls):
        cls._mock = None
        del cls._mock
