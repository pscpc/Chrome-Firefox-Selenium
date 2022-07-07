from seleniumwire import webdriver
import time
options = {
    'proxy': {
        'http': 'http://username:password@ip:port',
        'https': 'https://username:password@ip:port',
        'no_proxy': 'localhost,127.0.0.1'
    }
}
driver = webdriver.Chrome("ChromeSelenium/chromedriver.exe",seleniumwire_options=options)
driver.get('http://www.whatsmyip.org/')
time.sleep(9999)