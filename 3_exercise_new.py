from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

service = ChromeService("c:\piton loyiha\seleium\chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(("disable-blink-features=AutomationControlled"))
    driver=webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


def main():
    driver = get_driver()
    time.sleep(4)
    driver.find_element(by="id", value="CustomerEmail").send_keys("sanjarbek.89.ss@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="CustomerPassword").send_keys("123456789"+Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    return driver

print(main())





