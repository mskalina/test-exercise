from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def insert_bin_and_click(self, test_bin):
        bin_input = self.driver.find_element(By.CSS_SELECTOR, "#bin_number")
        bin_input.send_keys(test_bin)
        apply_button = self.driver.find_element(By.CSS_SELECTOR, "[name='Submit']")
        apply_button.click()

    def check_wait_for_response_message(self):
        WebDriverWait(self.driver, 15).until_not(
            ec.presence_of_element_located((By.XPATH, "//td[contains(text(),'WAIT FOR RESPONSE')]")),
            "Response did not appear on time")

    def check_there_are_no_error_messages(self):
        WebDriverWait(self.driver, 2).until_not(
            ec.presence_of_element_located((By.XPATH, "//td[contains(text(),'ERROR')]")),
            "Error in response")

    def wait_for_not_found_message(self):
        WebDriverWait(self.driver, 15).until(
            ec.presence_of_element_located((By.XPATH, "//td[contains(text(),'NOT FOUND')]")),
            "There is no expected <NOT FOUND> message in the field(s) without information")

    def check_there_is_error_message(self):
        error_text = self.driver.find_element(By.ID, "error")
        element_text = error_text.text
        return element_text
