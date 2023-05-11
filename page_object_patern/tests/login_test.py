import pytest

from page_object_patern.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("sialalala@gmail.com", "Tester12345!@#$%")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("sialalala1@gmail.coml", "Tester12345!@#$%")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
