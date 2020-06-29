from pom.aut import AUT


class BasePage:

    url = None
    
    def __init__(self):
        self.driver = AUT.driver

    def navigate_to(self):
        self.driver.get(self.url)
        
    def get_title(self):
        return self.driver.title