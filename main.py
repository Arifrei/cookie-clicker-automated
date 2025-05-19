from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
def click_cookie():
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

def buy_items():
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")
    cookies_element = driver.find_element(By.ID, "money").text
    if "," in cookies_element:
        cookies_element = cookies_element.replace(",", "")
    cookies = int(cookies_element)
    locator = None
    for item in store_items:
        cost_element = item.find_element(By.TAG_NAME, "b")
        cost = cost_element.text.split("-")[1]
        if "," in cost:
            cost = cost.replace(",", "")
        if int(cost) < cookies:
            locator = item.get_attribute("id")
    if locator:
        item_to_buy = driver.find_element(By.ID, locator)
        item_to_buy.click()

start_time = time.time()
while True:
    click_cookie()
    if time.time() - start_time > 2.5:
        buy_items()
        start_time = time.time()

# driver.quit()








# input("Press Enter after solving CAPTCHA...")
# price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]').text
# print(price_dollar)

# event_date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {n + 1: {"time": event_date[n].text, "event": event_name[n].text} for n in range(len(event_date))}
# print(events)

# close specific tab
# driver.close()
# close entire browser
# driver.quit()