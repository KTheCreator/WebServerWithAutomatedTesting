from locator import *
from element import BasePageElement
#This script handles the creation and functionality of the pages and their tests.

class BasePage(object):#Initialises the base for the pages to inherit
    def __init__(self, driver):
        self.driver = driver

class UsernameFieldElement(BasePageElement):#Inherits from the BasePageElement class to find and obtain the attributes of the targeted elements
    locator = "username"

class InputPage(BasePage):#Handles the testing for the InputPage
    #Sets the resulting web element to this variable
    userField = UsernameFieldElement()

    def click_submit_button(self):#Fucntionailty to simulate user clicking on the submit button
        #Obtains the location of the submit button from the InputPageLocators class
        element = self.driver.find_element(*InputPageLocators.SUBMIT_BUTTON)
        #Clicks submit button
        element.click()

    def titleMatching(self):#Test for the title being correct on the page
        return "WebProject" in self.driver.title
        
class ResultPage(BasePage):#Handles the testing for the results page
    
    def does_input_and_results_match(self,uIn):#Checks if the user's string is being displayed in the targeted element
        #Finds element
        target = self.driver.find_element(*ResultPageLocators.RESULTS_DISPLAY)
        #Returns results
        return uIn in target.text
    
    
