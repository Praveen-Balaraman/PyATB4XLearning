from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alerts():


    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a").click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    a = driver.switch_to.alert
    print(driver.switch_to.alert.text)
    a.accept()


    time.sleep(5)

test_alerts()