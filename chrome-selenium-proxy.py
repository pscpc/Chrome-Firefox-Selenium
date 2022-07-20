from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = {
    'proxy': {
        'http': 'http://username:password@ip:port',
        'https': 'https://username:password@ip:port',
        'no_proxy': 'localhost,127.0.0.1'
    }
}
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("ChromeSelenium/chromedriver.exe",seleniumwire_options=options,options=chrome_options)
driver.get('http://www.whatsmyip.org/')
time.sleep(9999)