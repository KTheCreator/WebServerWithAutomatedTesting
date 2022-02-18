from selenium.webdriver.common.by import By
#This scripts stores all the elements' location; simply for ease for the programming to ahve a constant reference to the element
class InputPageLocators(object):#For the input page
    SUBMIT_BUTTON = (By.ID, "submit")#Stores the submit button 
    USERNAME_FIELD = (By.ID,"username")#Stores the user input field element

class ResultPageLocators(object):#For the Result Page
    RESULTS_DISPLAY = (By.ID,"results")#Stores the element displaying the user's name
