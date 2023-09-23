from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
service = ChromeService("c:\piton loyiha\seleium\chromedriver.exe")
def get_driver():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    element = float(text.split(":")[1])
    return element

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())
