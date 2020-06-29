from pom.base_page import BasePage

class Dashboard(BasePage):

    def is_at(self):
        
        classHead = self.driver.find_element_by_class_name("head")
        textClassHead = classHead.text
        #print(textClassHead)
        
        #h1s = self._driver.find_element_by_tag_name("h1")
        #print(h1s.text)
        
        return textClassHead == "Dashboard"


