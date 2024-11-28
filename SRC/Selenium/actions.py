import time

from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.pointer_actions import MouseButton


def test_actions():
    driver =webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    username=driver.find_element(By.ID,"username")

    action=ActionChains(driver=driver)
    action.key_down(Keys.SHIFT).send_keys_to_element(username,"student").key_up(Keys.SHIFT).perform()
    time.sleep(5)
    password = driver.find_element(By.ID, "password")
    action.key_down(Keys.SHIFT).send_keys_to_element(password,"Password123").key_up(Keys.SHIFT).perform()
    time.sleep(5)
    a=ActionBuilder(driver=driver)
    driver.find_element(By.ID,"submit")
    a.pointer_action.pointer_down(MouseButton.LEFT)
    a.perform()
time.sleep(5)



