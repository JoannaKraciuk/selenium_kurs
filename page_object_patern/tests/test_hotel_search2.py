import allure
import pytest
from page_object_patern.pages.search_hotel import SearchHotelPage
from page_object_patern.pages.search_results import SearchResultsPage


@pytest.mark.usefixtures("setup")
class TestHotelSearch:
    @allure.title("This is title")
    @allure.description("Test description")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("15/05/2023", "16/05/2023")
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert price_values[0] == "0"
        assert price_values[1] == "0"
        assert price_values[2] == "0"
        assert price_values[3] == "0"
