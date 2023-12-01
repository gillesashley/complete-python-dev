from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create an Options object and set the detach option to True
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome browser instance with the options parameter
chrome_browser = webdriver.Chrome(options=options)

chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/")

chrome_browser.implicitly_wait(0.5)
text_box = chrome_browser.find_element(by=By.ID, value="edit-search-block-form--2")
text_box.send_keys("Automation With Selenium is sweet")

assert "Automation With Selenium" in chrome_browser.title
art_btn = chrome_browser.find_element(by=By.LINK_TEXT, value="SELENIUM ARTICLES")
art_btn.click()

chrome_browser.quit()
