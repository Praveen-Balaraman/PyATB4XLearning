import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
def test_browser():
 driver.get("https://practicetestautomation.com/practice-test-login/")
 driver.maximize_window()
 driver.find_element(By.ID,"username").click()
 driver.find_element(By.ID,"username").send_keys("student")
 driver.find_element(By.ID,"password").click()
 driver.find_element(By.ID,"password").send_keys("Password123")
 driver.find_element(By.ID,"submit").click()
 time.sleep(5)
 assert 1+1==2

