from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


try:
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.ID,"how are you")

except NoSuchElementException as nse:
  #  NoSuchElementException as
    print(nse.msg)