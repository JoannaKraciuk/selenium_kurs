from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select
import allure

from page_object_patern.locators.locators import BillingAddressLocators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        # Billing Address Page elements
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.company_input = BillingAddressLocators.company_input
        self.country_select = BillingAddressLocators.country_select
        self.addresses_link = BillingAddressLocators.addresses_link
        self.edit_link = BillingAddressLocators.edit_link
        self.addresses_input = BillingAddressLocators.addresses_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.message_div = BillingAddressLocators.message_div

    @allure.step("Open billing address page")
    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    @allure.step("Set personal data to (1), (2)")
    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set personal data", attachment_type=AttachmentType.PNG)

    @allure.step("Set company name to (1)")
    def set_company_name(self, company):
        self.driver.find_element(*self.company_input).send_keys(company)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set company name", attachment_type=AttachmentType.PNG )

    @allure.step("Select country to (1)")
    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)
        allure.attach(self.driver.get_screenshot_as_png(), name="Select country", attachment_type=AttachmentType.PNG)

    @allure.step("Set address to (1), (2), (3)")
    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.addresses_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set address", attachment_type=AttachmentType.PNG)

    @allure.step("Set phone number to (1)")
    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    @allure.step("Save address")
    def save_address(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element())
        self.driver.find_element(*self.save_address_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Save address", attachment_type=AttachmentType.PNG)

    @allure.step("Get message text")
    def get_message_text(self):
        return self.driver.find_element(*self.message_div).text