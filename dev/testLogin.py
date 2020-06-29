from config.conf import setup_env
from pom import driver
from pom.login import LoginPage
from pom.aut import AUT,init_browser

    
def testLogin():
    
    setup_env('dev')
    
    AUT.driver = init_browser()
    #driver1 = driver.init_browser()
    
    loginPage = LoginPage()
    loginPage.navigateTo()
    isAtLoginPage = loginPage.isAt()
    print("Is at Login Page : " + str(isAtLoginPage))
    
    dash1 = loginPage.login("Admin","admin123")
    loggedIn = loginPage.isLoggedIn("Admin")
    print("loggedIn : " + str(loggedIn))
    
    isAtDash = dash1.isAt()
    print("Is at Dashboard : " + str(isAtDash))
    
    AUT.closeDriver()
    
    
    print("Test login done")
    


if __name__ == '__main__':
    
    testLogin()