from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)
driver.maximize_window()
search_input = driver.find_element(By.CLASS_NAME, "header-search-button")


time.sleep(5)
search_input.click()
search_input = driver.find_element(By.ID, "query-builder-test")

search_input.send_keys("python")
time.sleep(2)
search_input.send_keys(Keys.ENTER)

time.sleep(10)
driver.close()
