import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elementLocator import *
from data import *

class DemoBlazeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.demoblaze.com/")

    def testContactValidWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))        
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh()        

    def testContactInvalidEmailWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(invalid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactOffensiveWordWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(offensive_word_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 
    
    def testContactEmptyEmailWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(empty_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactEmptyNameWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(empty_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactEmptyMsgWithoutLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(empty_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh()
        
    def testLogin(self):
        wait = WebDriverWait(self.driver, 10)
        login_link = wait.until(EC.element_to_be_clickable(pageLocators.LOGIN_LINK))
        self.driver.execute_script("arguments[0].click();", login_link)
        try:
            wait.until(EC.visibility_of_element_located(pageLocators.LOGIN_MODAL))
        except TimeoutException:
            print("Timed out waiting for login modal to become visible")
            raise
        username_field = wait.until(EC.visibility_of_element_located(pageLocators.USERNAME_FIELD))
        self.driver.execute_script(f"arguments[0].value='{valid_username_login}';", username_field)
        password_field = wait.until(EC.visibility_of_element_located(pageLocators.PASSWORD_FIELD))
        password_field.send_keys(valid_password_login)
        self.driver.find_element(*pageLocators.LOGIN_BUTTON).click()
        time.sleep(5)
        self.driver.refresh()
        
    def testContactValidWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))        
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh()        

    def testContactInvalidEmailWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(invalid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactOffensiveWordWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(offensive_word_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 
    
    def testContactEmptyEmailWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(empty_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactEmptyNameWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(empty_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(contact_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh() 

    def testContactEmptyMsgWithLogin(self):
        wait = WebDriverWait(self.driver, 10)
        contact_link = wait.until(EC.element_to_be_clickable(ContactPageLocators.CONTACT_LINK))
        contact_link.click()
        wait.until(EC.visibility_of_element_located(ContactPageLocators.RECIPIENT_EMAIL_FIELD))
        self.driver.find_element(*ContactPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(valid_email_contact)
        self.driver.find_element(*ContactPageLocators.RECIPIENT_NAME_FIELD).send_keys(valid_contactname_contact)
        self.driver.find_element(*ContactPageLocators.MESSAGE_TEXT_FIELD).send_keys(empty_message_contact)
        self.driver.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(5)
        self.driver.refresh()
    
def sort_test_methods(self, method1, method2):
    order = {
        "testContactValidWithoutLogin": 0,
        "testContactInvalidEmailWithoutLogin": 1,
        "testContactOffensiveWordWithoutLogin": 2,        
        "testContactEmptyEmailWithoutLogin": 3,
        "testContactEmptyNameWithoutLogin": 4,
        "testContactEmptyMsgWithoutLogin": 5,
        "testLogin": 6,
        "testContactValidWithLogin": 7,
        "testContactInvalidEmailWithLogin": 8,
        "testContactOffensiveWordWithLogin": 9,
        "testContactEmptyEmailWithLogin": 10,
        "testContactEmptyNameWithLogin": 11,
        "testContactEmptyMsgWithLogin": 13
    }
    return order[method1] - order[method2]

unittest.TestLoader.sortTestMethodsUsing = sort_test_methods    

if __name__ == "__main__":
    unittest.main()
