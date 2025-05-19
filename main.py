import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
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
    cookies_element = driver.find_element(By.ID, "money").text.replace(",", "")
    cookies = int(cookies_element)
    affordable_items = []
    for item in store_items:
        cost_element = item.find_element(By.TAG_NAME, "b")
        cost = cost_element.text.split("-")[1].replace(",", "").strip()
        if int(cost) <= cookies:
            affordable_items.append((cost, item.get_attribute("id")))
    if affordable_items:
        most_expensive = max(affordable_items, key=lambda x: x[0])
        try:
            item_to_buy = driver.find_element(By.ID, most_expensive[1])
            item_to_buy.click()
        except selenium.common.exceptions.StaleElementReferenceException:
            time.sleep(0.1)
            item_to_buy = driver.find_element(By.ID, most_expensive[1])
            item_to_buy.click()


start_time = time.time()
end_time = time.time() + 600
while time.time() < end_time:
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