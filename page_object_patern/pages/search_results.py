from allure_commons.types import AttachmentType
from page_object_patern.locators.locators import SearchResultLocators
import allure
import logging
class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath

    @allure.step("Checking results")
    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Avaliable hotels are: ")
        for name in names:
            self.logger.info(name)
        return names
        allure.attach(self.driver.get_screenshot_as_png(), name="Results", attachment_type=AttachmentType.PNG)

    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        price_values = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices are: ")
        for price in prices:
            self.logger.info(price)
        return price_values