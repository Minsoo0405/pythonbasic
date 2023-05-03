import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("http://3.37.135.228/common/login/")

time.sleep(5)
form_elements = driver.find_elements(By.CLASS_NAME, "form-control")
form_elements[0].send_keys("minsoo")
time.sleep(5)
form_elements[1].send_keys("munsi0405")
time.sleep(5)
# driver.find_elements(By.TAG_NAME, "button")[1].click()
driver.find_elements(By.LINK_TEXT, "로그인")[1].click()
time.sleep(10)