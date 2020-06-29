
from config.conf import env
from pom.dashboard import Dashboard
from pom.base_page import BasePage

class LoginPage(BasePage):
    
    #url = env['url_demo']
    url = "https://opensource-demo.orangehrmlive.com/"

    def login(self, name, pwd):
        
        inputUserName = self.driver.find_element_by_id("txtUsername")
        inputUserName.clear()
        inputUserName.send_keys(name)
    
        inputPassword = self.driver.find_element_by_id("txtPassword")
        inputPassword.clear()
        inputPassword.send_keys(pwd)
    
        btnLogin = self.driver.find_element_by_id("btnLogin")
        btnLogin.click()
             
        return Dashboard()
    
    def is_logged_in(self, name):
        
        welcomeText = self.driver.find_element_by_id("welcome")
                
        return name in welcomeText.text
