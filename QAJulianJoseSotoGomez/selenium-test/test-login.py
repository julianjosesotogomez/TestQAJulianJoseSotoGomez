from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='C:/Users/julia/OneDrive/Escritorio/QAJulianJoseSotoGomez/selenium-test/chromedriver_win32/chromedriver.exe')
        driver =self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_login_page(self):
        driver =self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Login In').click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password =driver.find_element_by_id('password')
        confirm_passwrod = driver.find_element_by_id('confirmation')
        news_latter_subscription = driver.find_element_by_id('is_suscribed')
        submit_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

        self.assertTrue(first_name.is_enabled() and last_name.is_enabled()
                                                and middle_name.is_enabled()
                                                and email_address.is_enabled()
                                                and password.is_enabled()
                                                and confirm_passwrod.is_enabled()
                                                and news_latter_subscription.is_enabled()
                                                and submit_button.is_enabled())

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        email_address.send_keys('Test')
        password.send_keys('Test')
        confirm_passwrod.send_keys('Test')
        news_latter_subscription.send_keys('Test')
        submit_button.click()


    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)     