import pytest
from selenium import webdriver
from main_page import MainPage

# TO DO: to improve link can be set by arguments when running tests
LINK = "http://localhost:8080/"
# TO DO: test bins should be chosen randomly to improve test results
TEST_BIN_FULL = "300234"
TEST_BIN_NOT_FULL = "103003"


@pytest.fixture(scope="function")
def open_browser():
    driver = webdriver.Chrome()
    page = MainPage(driver, LINK)
    page.open()
    yield page
    page.close()


def test_check_returned_full_data(open_browser):
    page = open_browser
    page.insert_bin_and_click(TEST_BIN_FULL)
    page.check_wait_for_response_message()
    page.check_there_are_no_error_messages()


def test_check_returned_partly_data(open_browser):
    page = open_browser
    page.insert_bin_and_click(TEST_BIN_NOT_FULL)
    page.wait_for_not_found_message()


def test_empty_bin(open_browser):
    page = open_browser
    page.insert_bin_and_click("")
    page.check_wait_for_response_message()
    error_text = page.check_there_is_error_message()
    assert error_text == "BIN number can't be empty", "Error message is not correct or empty"
