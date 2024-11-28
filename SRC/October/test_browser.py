import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
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
