from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select
import allure
from page_object_patern.locators.locators import ShopPage

class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        #Shop Page Elemnts
        self.shop_button = ShopPage.shop_button
        self.add_to_cart_button = ShopPage.add_to_cart_button
        self.view_cart = ShopPage.view_cart
        self.proceed_to_checkout_button= ShopPage.proceed_to_checkout
        self.billing_first_name = ShopPage.billing_first_name
        self.billing_last_name = ShopPage.billing_last_name

    @allure.step("Open shop page")
    def open_shop_page(self):
        self.driver.find_element(*self.shop_button).click()

    @allure.step("Add to cart")
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        self.driver.find_element(*self.view_cart).click()

    @allure.step("Proceed do checkout")
    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()
