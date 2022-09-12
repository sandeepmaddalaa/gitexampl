import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "jksandeep515"  # Replace the username
access_key = "odbX0VyAYifj4HPaCZA849bVKimsTQXToG392Gx5WbGqMpkhTp"  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build":'lambdatest1',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "browserName": 'Chrome',
            "version": '105.0',
            "platform": 'Windows 10',
            "resolution": '1024x768',
            "console": 'true',  # Enable or disable console logs
            "network": 'true'  # Enable or disable network logs
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities=desired_caps)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get('https://www.lambdatest.com/selenium-playground')

        driver.find_element(By.PARTIAL_LINK_TEXT, "Simple Form Demo").click()
        driver.find_element(By.ID, "user-message").send_keys("Welcome to Lambdatest")
        driver.find_element(By.ID, "showInput").click()
        lamp = driver.find_element(By.ID, "message").text
        if lamp == 'Welcome to Lambdatest':
            print("True")
        else:
            print("False")
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
