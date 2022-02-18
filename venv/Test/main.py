import unittest
from selenium import webdriver
import page
#The script handles the running of the tests using selenium and python unit testing module
class webProject(unittest.TestCase):

    def setUp(self):#Sets up the testing environment
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")#Opens in chrome
        self.driver.get("http://127.0.0.1:5000/input")#Connects to the webserver

    #This function is the main test that simulates the user inputting a string and displaying it on the other page
    def test_input_field(self):
        testInput = "Kline"#Test Input - Included for scalability so a set of strings can be tested and multiple times
        inputPage = page.InputPage(self.driver)#Creates an instance of the input page on the driver
        assert inputPage.titleMatching()#Runs test to see if the title matches
        inputPage.userField = testInput
        inputPage.click_submit_button()#Submits the test input in the form
        resultPage = page.ResultPage(self.driver)
        assert resultPage.does_input_and_results_match(testInput)#Checks if the user's input is on the results page

    def tearDown(self):
        self.driver.close()#Closes instance of the testing environment

if __name__ == "__main__":
    unittest.main()
