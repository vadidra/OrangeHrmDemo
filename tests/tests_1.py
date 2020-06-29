import HtmlTestRunner
import unittest


class ExampleTest1(unittest.TestCase):
    """ Example test for HtmlRunner. """

    @classmethod
    def setUpClass(cls):
        print("Tests-1 - set up class")
        #self.assertEqual('foo'.upper(), 'FOO')
        
    @classmethod
    def tearDownClass(cls):
        print("Tests-1 - tear down class")

    def test_11(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_12(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_13(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
