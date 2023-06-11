from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("http://seleniumdemo.com/")
driver.find_element(By.XPATH, "//li[@id='menu-item-21']//span").click()
driver.find_element(By.LINK_TEXT, "Add to cart").click()
driver.find_element(By.XPATH, "//div[@id='content']//a[3]").click()
driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
driver.find_element(By.ID, "billing_first_name").send_keys("Martin")
driver.find_element(By.ID, "billing_last_name").send_keys("Soho")
#driver.find_elements(By.ID, "select2-billing_country-container").is_selected("Poland")



driver.quit()

