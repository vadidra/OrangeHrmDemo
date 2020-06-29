import unittest
from pom.login import LoginPage


class TestLogin(unittest.TestCase):
    """ Example test for HtmlRunner. """
    
    @classmethod
    def setUpClass(cls):
        cls.login_page = LoginPage()
        cls.dashboard = None
        
    @classmethod
    def tearDownClass(cls):
        cls.login_page = None
        cls.dashboard = None

    def test_01_navigate_to_login_page(self):
        
        TestLogin.login_page.navigate_to()
        self.assertTrue(TestLogin.login_page.get_title() == 'OrangeHRM', "Not at Login page")
        
    def test_02_login(self):
        
        TestLogin.dashboard = TestLogin.login_page.login("Admin","admin123")
        self.assertTrue(TestLogin.login_page.is_logged_in("Admin"), "Not logged in")
        
    def test_03_at_Dashboard(self):

        self.assertTrue(TestLogin.dashboard.is_at(), "Not at Dashboard")

