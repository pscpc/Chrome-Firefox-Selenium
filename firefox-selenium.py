from re import T
from selenium import webdriver

url = "https://google.com"
driver = webdriver.Firefox()
foxyproxy = "foxyproxy_standard-7.5.1.xpi"
driver.install_addon(foxyproxy, temporary=True)
driver.profile = webdriver.FirefoxProfile()
driver.profile.add_extension(foxyproxy)
driver.profile.set_preference("security.fileuri.strict_origin_policy", False)
driver.profile.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
driver.profile.update_preferences()

driver.get(url)