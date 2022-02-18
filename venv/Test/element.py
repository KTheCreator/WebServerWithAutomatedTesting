from selenium.webdriver.support.ui import WebDriverWait
#This aspect of the solution I am not entirely confident with as it did come from a tutorial (https://www.youtube.com/watch?v=O_sIPPA4euw)

class BasePageElement(object):#Handles the process of getting and setting the values of targetted elements 

    def __set__(self,obj,value):#Handles the setting of the elements value

        driver = obj.driver#Not entirely sure
        #WebDriver will wait till the program finds the element by its ID
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(self.locator))
        #Clears the field, in case it has a value already, and sets a new value given as a parameter
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self,obj,owner):#Handles the getting process of the element
        driver = obj.driver
        #WebDriver will wait till the program finds the element by its ID
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(self.locator))
        #Gets the targeted element and returns its attributes
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")
