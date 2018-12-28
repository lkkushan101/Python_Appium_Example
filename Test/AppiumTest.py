import os
import unittest
from time import sleep
from appium import webdriver


class ContactAppTestAppium(unittest.TestCase):


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'AVY9KA9631900412'
        desired_caps['appPackage'] = 'com.experitest.ExperiBank'
        desired_caps['appActivity'] = '.LoginActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def tearDown(self):
        "Tear down the test"
        self.driver.quit()


    def test_single_player_mode(self):
        "Test the Chess app launches correctly and click on Play button"
        elementUserName = self.driver.find_element_by_id("com.experitest.ExperiBank:id/usernameTextField")
        elementUserName.send_keys("company")
        elementUserPassword = self.driver.find_element_by_id("com.experitest.ExperiBank:id/passwordTextField")
        elementUserPassword.send_keys("company")
        elementLoginBtn = self.driver.find_element_by_id("com.experitest.ExperiBank:id/loginButton")
        elementLoginBtn.click()

        sleep(5)


