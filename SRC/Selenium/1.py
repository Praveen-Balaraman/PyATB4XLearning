import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(1000)
title=driver.title
print(title)
url=driver.current_url
print(url)
#driver.find_element(By), "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a"

(WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div/div[3]/div[1]/a[1]/button")))).click()

#(WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))


driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
time.sleep(100)