import HtmlTestRunner
import unittest


class ExampleTest2(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_21(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_22(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_23(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

