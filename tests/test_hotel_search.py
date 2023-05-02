import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_patern.pages.search_hotel import SearchHotelPage

class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_serch(self,setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("01/05/2023", "06/05/2023")
        search_hotel_page.set_travellers("2","2")
        search_hotel_page.perfom_search()





