import unittest
from pom.aut import AUT,init_browser


class TestPrecondition(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_init_driver(self):
        
        AUT.driver = init_browser()
        self.assertIsNotNone(AUT.driver, "AUT driver is None")



