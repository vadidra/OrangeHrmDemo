'''
Application under test
'''

from selenium import webdriver

def init_browser():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--test-type")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
        
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
        
    des_cap = {}
        
    driver = webdriver.Chrome(executable_path=r'C:\software\chromedriver.exe',
                              options = options,
                              desired_capabilities = des_cap )
    
    return driver

class AUT(object):
    
    driver = None
    
    @classmethod
    def close_browser(cls):
        
        if AUT.driver is not None:
            AUT.driver.close()
            AUT.driver = None
            print('Browser closed')


    def __init__(self):
        pass
    
    

