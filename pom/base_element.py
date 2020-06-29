from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Baselement:
    
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)
        
        self.web_element = None
        self.find()
        
    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        self.web_element = element
        
    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        element.click()
        
    @property
    def text(self):
        text1 = self.web_element.text
        return text1
    
    def get_text(self):
        text1 = self.web_element.text
        return text1
    
    def input_text(self, text):
        self.web_element.send_keys(text)
        
    def get_attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
        