from pythonmonitorurl import *
import unittest

class TestURL(unittest.TestCase):
    def test_get_url_status(self):
        self.assertAlmostEqual(get_url_status('https://httpstat.us/200'),1)
        self.assertAlmostEqual(get_url_status('https://httpstat.us/503'),0)
        self.assertAlmostEqual(get_url_status('https://httpstat.us/400'),0)


