import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

username = "jksandeep515"  # Replace the username
access_key = "odbX0VyAYifj4HPaCZA849bVKimsTQXToG392Gx5WbGqMpkhTp"  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build":'lambda-test-3',  # Change your build name here
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

        driver.find_element(By.PARTIAL_LINK_TEXT, "Input Form Submit").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "btn").click()
        #assert "Please fill in the fields"

        driver.find_element(By.ID, "name").send_keys("Sandeep")
        driver.find_element(By.ID, "inputEmail4").send_keys("sandeepmaddalaa@gmail.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("Sandeep@143")
        driver.find_element(By.ID, "company").send_keys("Mindtree")
        driver.find_element(By.ID, "websitename").send_keys("Lambdatest.com")
        city = driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[3]/div[1]/select')
        dropdown = Select(city)
        dropdown.select_by_visible_text("India")
        driver.find_element(By.ID, "inputCity").send_keys("sr nagar")
        driver.find_element(By.ID, "inputAddress1").send_keys("near mindtree")
        driver.find_element(By.ID, "inputAddress2").send_keys("HYd")
        driver.find_element(By.XPATH, '//*[@id="inputState"]').send_keys("telengana")
        driver.find_element(By.ID, "inputZip").send_keys("500038")
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "btn").click()

        Thanks = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div/p').text
        print(Thanks)


if __name__ == "__main__":
    unittest.main()
