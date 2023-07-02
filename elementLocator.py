from selenium.webdriver.common.by import By

############### SIGN UP ###############

class SignupPageLocators:
    SIGNUP_LINK = (By.ID, "signin2")
    SIGNUP_MODAL = (By.ID, "signInModal")
    USERNAME_FIELD = (By.ID, "sign-username")
    PASSWORD_FIELD = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[@onclick='register()']")


############### SIGN UP ###############

############### LOGIN - LOGOUT ###############

class pageLocators:
    LOGIN_LINK = (By.ID, "login2")
    LOGIN_MODAL = (By.ID, "logInModal")
    LOGOUT_LINK = (By.ID, "logout2")
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[@onclick='logIn()']")
    
############### LOGIN - LOGOUT ###############

############### ADD TO CART ###############

class ProductPageLocators:    
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@onclick='addToCart(1)']")

    PRODUCT_NAME = (By.XPATH, "//h2[@class='name']")

class CartPageLocators:
    CART_LINK = (By.ID, "cartur")
    CART_MODAL = (By.ID, "exampleModal")
    CART_TABLE = (By.ID, "tbodyid")
    PRODUCT_NAME_CELLS = (By.XPATH, "//table[@id='tbodyid']//td[2]")

############### ADD TO CART ###############    

############### CART ###############  

class cartPage():
    idLoginPage = (By.ID,"login2")
    idUsername = (By.ID,"loginusername")
    idPassword = (By.ID,"loginpassword")
    buttonLogin = ("xpath", "//button[contains(text(),'Log in')]")
    linkCartPage = (By.LINK_TEXT, "Cart")
    linkSamsung = (By.LINK_TEXT, "Samsung galaxy s6")
    linkAddToCart = (By.LINK_TEXT, "Add to cart")
    linkHome = (By.XPATH, "//a[contains(text(),'Home')]")
    linkNokia = (By.LINK_TEXT,"Nokia lumia 1520")
    linkDelete = (By.LINK_TEXT,"Delete")
    linkLogout = (By.LINK_TEXT, "Log out")
    linkNexus = (By.LINK_TEXT,"Nexus 6")

############### CART ###############  

############### CONTACT ############### 

class ContactPageLocators:
    CONTACT_LINK = (By.XPATH, "//a[text()='Contact']")
    RECIPIENT_EMAIL_FIELD = (By.ID, "recipient-email")
    RECIPIENT_NAME_FIELD = (By.ID, "recipient-name")
    MESSAGE_TEXT_FIELD = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[text()='Send message']")

############### CONTACT ############### 

############### PLACE ORDER ############### 

class PlaceOrderLocators:
    PRODUCT_LINK = (By.CSS_SELECTOR, 'a[href*="prod.html?idp_="]')
    CART_LINK = (By.CSS_SELECTOR, 'a[href*="cart.html"]')
    MODAL_BODY = (By.CLASS_NAME, "modal-body")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'a[onclick*="addToCart"]')
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-success[data-target="#orderModal"]')
    NAME_INPUT = (By.ID, 'name')
    COUNTRY_INPUT = (By.ID, 'country')
    CITY_INPUT = (By.ID, 'city')
    CARD_INPUT = (By.ID, 'card')
    MONTH_INPUT = (By.ID, 'month')
    YEAR_INPUT = (By.ID, 'year')
    PURCHASE_BUTTON = (By.CSS_SELECTOR, 'button[onclick*="purchaseOrder()"]')

############### PLACE ORDER ###############