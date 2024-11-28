from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import time
ignore_list=[ElementNotVisibleException,ElementNotSelectableException]
driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.maximize_window()
driver.find_element(By.ID,"login-username").send_keys("abc@gmail.com")
driver.find_element(By.ID,"login-password").send_keys("password@1234")
driver.find_element(By.ID,"js-login-btn").click()
#time.sleep(10)
WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.ID,"js-notification-box-msg")))
WebDriverWait(driver=driver,poll_frequency=1, timeout=5,ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.ID,"js-notification-box-msg")))
time.sleep(10)

