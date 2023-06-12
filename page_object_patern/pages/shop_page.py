from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select
import allure
from page_object_patern.locators.locators import ShopPage

class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        #Shop Page Elements
        self.shop_button = ShopPage.shop_button
        self.add_to_cart_button = ShopPage.add_to_cart_button
        self.view_cart = ShopPage.view_cart
        self.proceed_to_checkout_button= ShopPage.proceed_to_checkout
        self.billing_first_name = ShopPage.billing_first_name
        self.billing_last_name = ShopPage.billing_last_name
        self.billing_address = ShopPage.billing_address
        self.billing_postcode = ShopPage.billing_postcode
        self.billing_city = ShopPage.billing_city
        self.billing_phone = ShopPage.billing_phone
        self.billing_email = ShopPage.billing_email
        self.place_order = ShopPage.place_order

    @allure.step("Open shop page")
    def open_shop_page(self):
        self.driver.find_element(*self.shop_button).click()

    @allure.step("Add to cart")
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        self.driver.find_element(*self.view_cart).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add to cart", attachment_type=AttachmentType.PNG)


    @allure.step("set_first_name to (1), last_name to (2), address to (3), postcode to (4), city to (5), phone to (6),"
                 " email to (7), ")
    def proceed_to_checkout(self, first_name, last_name, address, postcode, city, phone, email):
        self.driver.find_element(*self.proceed_to_checkout_button).click()
        self.driver.find_element(*self.billing_first_name).send_keys(first_name)
        self.driver.find_element(*self.billing_last_name).send.keys(last_name)
        self.driver.find_element(*self.billing_address).send.keys(address)
        self.driver.find_element(*self.billing_postcode).send.keys(postcode)
        self.driver.find_element(*self.billing_city).send.keys(city)
        self.driver.find_element(*self.billing_phone).send.keys(phone)
        self.driver.find_element(*self.billing_email).send.keys(email)
        self.driver.find_element(*self.place_order).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_first_name, last_name, address, ppotcode, city, "
                                                                "phone, email", attachment_type=AttachmentType.PNG)

        


