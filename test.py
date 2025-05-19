from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")
# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# portals = driver.find_element(By.LINK_TEXT, "Content portals")
name = driver.find_element(By.NAME, "fName")
name.send_keys("Aron", Keys.TAB, "Freilich", Keys.TAB, "test@test.com", Keys.ENTER)

time.sleep(4)
driver.quit()