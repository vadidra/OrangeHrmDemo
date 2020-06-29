import unittest
from pom.aut import AUT
import time


class TestPostcondition(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_close_browser(self):
        
        AUT.close_browser()
        time.sleep(1)
        self.assertIsNone(AUT.driver, "AUT driver is not None")
