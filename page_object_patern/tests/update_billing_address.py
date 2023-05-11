import random

import pytest

from page_object_patern.pages.billing_address_page import BillingAddressPage
from page_object_patern.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0, 10000)) + "sialalala@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Tester12345!@#$%")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Doe")
        billing_address_page.set_company_name("NewOne")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Olchowa", "00-140", "Krakow")
        billing_address_page.set_phone_number("123456678")
        billing_address_page.save_address()

        assert "Address changed successfully." in billing_address_page.get_message_text()
