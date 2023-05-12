import random
import allure
import pytest
from page_object_patern.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @allure.title("Create account test")
    @allure.description("This test execute creating account with invalid data")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("sialalala@gmail.com", "Tester12345!@#$%")

        msg = "Error: An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_msg()

    @allure.description("This test execute creating account with valid data")
    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + "sialalala@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Tester12345!@#$%")

        assert my_account_page.is_logout_link_displayed()
