import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from elementLocator import *
import data
   
class DemoBlazeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.demoblaze.com/")

    def testValidPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")
        
    def testInvalidNamePlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.nameinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")
        
    def testInvalidCountryPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidCityPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidCreditCardPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidMonthPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidYearPlaceOrderWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearinvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")        

    def testInvalidPlaceOrderNotChoosingProductWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
                
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidPlaceOrderNullFormWithoutLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.emptyname_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.emptycountry_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.emptycity_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.emptycc_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.emptymonth_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.emptyyear_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
        except NoAlertPresentException:
            pass
        time.sleep(3)
        driver.refresh()
        
    def testLogin(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/index.html")
        wait = WebDriverWait(driver, 10)
        login_link = wait.until(EC.element_to_be_clickable(pageLocators.LOGIN_LINK))
        driver.execute_script("arguments[0].click();", login_link)
        try:
            wait.until(EC.visibility_of_element_located(pageLocators.LOGIN_MODAL))
        except TimeoutException:
            print("Timed out waiting for login modal to become visible")
            raise
        username_field = wait.until(EC.visibility_of_element_located(pageLocators.USERNAME_FIELD))
        driver.execute_script(f"arguments[0].value='{data.valid_username_login}';", username_field)
        password_field = wait.until(EC.visibility_of_element_located(pageLocators.PASSWORD_FIELD))
        password_field.send_keys(data.valid_password_login)
        driver.find_element(*pageLocators.LOGIN_BUTTON).click()
        time.sleep(5)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testValidPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")      
        
    def testInvalidNamePlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.nameinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")
        
    def testInvalidCountryPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidCityPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidCreditCardPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidMonthPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthinvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidYearPlaceOrderWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearinvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")        

    def testInvalidPlaceOrderNotChoosingProductWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
                
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.namevalid_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.countryvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.cityvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.ccvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.monthvalid_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.yearvalid_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        time.sleep(3)
        self.driver.get("https://www.demoblaze.com/index.html")

    def testInvalidPlaceOrderNullFormWithLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Add to cart
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product_link.click()
        
        wait.until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        
        time.sleep(5)        
        try:
            alert = driver.switch_to.alert            
            alert.dismiss()
        except NoAlertPresentException:            
            pass
        
        driver.refresh()
        
        # Place order
        cart_link = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.CART_LINK))
        cart_link.click()
        
        time.sleep(5)
        
        place_order_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PLACE_ORDER_BUTTON))
        place_order_button.click()
        
        wait.until(EC.visibility_of_element_located(PlaceOrderLocators.NAME_INPUT))
        driver.find_element(*PlaceOrderLocators.NAME_INPUT).send_keys(data.emptyname_placeorder)
        driver.find_element(*PlaceOrderLocators.COUNTRY_INPUT).send_keys(data.emptycountry_placeorder)
        driver.find_element(*PlaceOrderLocators.CITY_INPUT).send_keys(data.emptycity_placeorder)
        driver.find_element(*PlaceOrderLocators.CARD_INPUT).send_keys(data.emptycc_placeorder)
        driver.find_element(*PlaceOrderLocators.MONTH_INPUT).send_keys(data.emptymonth_placeorder)
        driver.find_element(*PlaceOrderLocators.YEAR_INPUT).send_keys(data.emptyyear_placeorder)
        
        purchase_button = wait.until(EC.element_to_be_clickable(PlaceOrderLocators.PURCHASE_BUTTON))
        purchase_button.click()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
        except NoAlertPresentException:
            pass
        time.sleep(3)        

def sort_test_methods(self, method1, method2):
    order = {
        "testValidPlaceOrderWithoutLogin": 0,
        "testInvalidNamePlaceOrderWithoutLogin": 1,
        "testInvalidCountryPlaceOrderWithoutLogin": 2,
        "testInvalidCityPlaceOrderWithoutLogin": 3,
        "testInvalidCreditCardPlaceOrderWithoutLogin": 4,
        "testInvalidMonthPlaceOrderWithoutLogin": 5,
        "testInvalidYearPlaceOrderWithoutLogin": 6,
        "testInvalidPlaceOrderNotChoosingProductWithoutLogin": 7,
        "testInvalidPlaceOrderNullFormWithoutLogin": 8,
        "testLogin": 9,
        "testValidPlaceOrderWithLogin": 10,
        "testInvalidNamePlaceOrderWithLogin": 11,
        "testInvalidCountryPlaceOrderWithLogin": 12,
        "testInvalidCityPlaceOrderWithLogin": 13,
        "testInvalidCreditCardPlaceOrderWithLogin": 14,
        "testInvalidMonthPlaceOrderWithLogin": 15,
        "testInvalidYearPlaceOrderWithLogin": 16,
        "testInvalidPlaceOrderNotChoosingProductWithLogin": 17,
        "testInvalidPlaceOrderNullFormWithLogin": 18
    }
    return order[method1] - order[method2]

unittest.TestLoader.sortTestMethodsUsing = sort_test_methods        
        
if __name__ == "__main__":
    unittest.main()