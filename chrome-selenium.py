from selenium import webdriver
import time
driver = webdriver.Chrome("ChromeSelenium/chromedriver.exe")
driver.get("https://www.python.org")
time.sleep(111)