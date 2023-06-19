from selenium.webdriver.common.by import By
import time

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        time.sleep(5)
        return self.driver.get(self.base_url) #в тесте не видит метод get не понимаю почему


    def find_element(self, locator):
        return self.find_element(By.CSS_SELECTOR, locator)
