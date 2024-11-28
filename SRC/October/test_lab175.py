import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_authentication():
    ...

@pytest.mark.smoke(reason="not completed")
def test_verify_sum():
    assert (1+1) == 2

@pytest.mark.smoke(reason="not completed")
def test_verify_sum1():
    assert (1+1) == 3
@pytest.mark.reg(reason="not completed")
def test_verify_sum2():
    assert (1+1) == 4
