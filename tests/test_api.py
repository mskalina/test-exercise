import pytest
import requests

# TO DO: to improve link can be set by arguments when running tests
LINK = "http://localhost:8080/"
GET_INFO = "get-info"
# TO DO: test binss should be chosen randomly to improve test results
TEST_BIN_FULL = "300234"
TEST_BIN_NOT_FULL = "103003"
UNKNOWN_BIN = "103004"
EXPECTED_FIELDS = ["bin", "brand", "type", "category", "issuer", "alpha_2", "alpha_3", "country", "latitude",
                   "longitude", "bank_phone", "bank_url"]


def test_post_with_empty_body():
    r = requests.post(LINK+GET_INFO, json={})
    r_data = r.json()
    assert r_data.get('detail') == "Empty request body"


def test_post_without_bin_in_body():
    r = requests.post(LINK+GET_INFO, json={"not_bin": TEST_BIN_FULL})
    r_data = r.json()
    assert r_data.get('detail') == "No 'bin_number' field in request"


@pytest.mark.parametrize("invalid_bin, error_text", [
    ("", "BIN number can't be empty"),
    ("23456", "BIN number's length can't be less than 6"),
    ("123456789", "BIN number's length can't be greater than 8"),
    ("stroka", "BIN number should contain only digits"),
    (234567, "BIN number should be string"),
    (UNKNOWN_BIN, "Unknown BIN")
])
def test_provide_invalid_bin_and_get_error(invalid_bin, error_text):
    r = requests.post(LINK+GET_INFO, json={"bin_number": invalid_bin})
    r_data = r.json()
    assert r_data.get('detail') == error_text


@pytest.mark.parametrize("valid_bin", [TEST_BIN_FULL, TEST_BIN_NOT_FULL])
def test_provide_valid_bin(valid_bin):
    r = requests.post(LINK+GET_INFO, json={"bin_number": valid_bin})
    r_data = r.json()
    if r_data.get('data') is not None:
        assert all(expected_field in r_data.get('data') for expected_field in EXPECTED_FIELDS), \
            "Body of response does not contain required fields"
    else:
        assert False, "Response did not return data"
