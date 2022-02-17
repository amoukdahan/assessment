# Anika Moukdahan
# QA Intern Legrand Assessment Challenge

import os
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert

from demoBlaze.Test.Flow.constants import BASE_URL


class Signup(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Signup, self).__init__(options=options)
        self.implicitly_wait(3)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(BASE_URL)

    # signing up, and logging in
    def register(self):
        username = input("Enter Username: ")
        print(username)
        password = input("Enter Password ")
        print(password)

        self.find_element_by_id('signin2').click()
        self.implicitly_wait(3)
        self.find_element_by_id('sign-username').send_keys(username)
        self.find_element_by_id('sign-password').send_keys(password)
        self.find_element_by_xpath('//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        self.find_element_by_id('frm').submit()
        self.implicitly_wait(3)

        self.refresh()
        self.find_element_by_xpath('//*[@id="login2"]').click()
        self.find_element_by_id('loginusername').send_keys(username)
        self.find_element_by_id('loginpassword').send_keys(password)
        self.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        self.implicitly_wait(3)

    # adding products to cart
    def select_product(self):
        self.refresh()
        self.find_element_by_xpath('//*[@id="itemc"]').click()
        self.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/a/img').click()

        self.implicitly_wait(3)
        self.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()
        self.find_element_by_id('cartur').click()
        self.implicitly_wait(10)
