from selenium.webdriver.common.by import By


class BillingAddressLocators:

    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    company_input = (By.ID, "billing_company")
    country_select = (By.ID, "billing_country")
    addresses_input = (By.ID, "billing_address_1")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    save_address_button = (By.XPATH, "//button[@value = 'Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")


class MyAccountPage:

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")
    logout_link = (By.LINK_TEXT, "Logout")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")

class ShopPage:

    shop_button = (By.XPATH, "//li[@id='menu-item-21']//span")
    add_to_cart_button = (By.LINK_TEXT, "Add to cart")
    view_cart = (By.XPATH, "//div[@id='content']//a[3]")
    proceed_to_checkout = (By.LINK_TEXT, "Proceed to checkout")
    billing_first_name = (By.ID, "billing_first_name")
    billing_last_name = (By.ID, "billing_last_name")
