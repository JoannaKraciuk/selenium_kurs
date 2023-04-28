class SearchHotelPage:

    def __init__(self,driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_span_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travelers_input_id = "travelersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    def set_city(self, city):
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_span_xpath).click()

    def set_date_range(self, check_in, check_out):

        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.checkout_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):

        self.driver.find_element_by_id(self.travelers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clean()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.child_input_id).clean()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)
        self.


        driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
        driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")
        driver.find_element_by_xpath("//span[text()='Dubai']").click()
        driver.find_element_by_name("checkin").send_keys("01/05/2023")
        driver.find_element_by_name("checkout").send_keys("06/05/2023")
        driver.find_element_by_id("travellersInput").click()
        driver.find_element_by_id("adultInput").clear()
        driver.find_element_by_id("adultInput").send_keys("3")
        driver.find_element_by_id("childInput").clear()
        driver.find_element_by_id("childInput").send_keys("3")
        driver.find_element_by_xpath("//button[text()=' Search']").click()