from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
service = ChromeService("c:\piton loyiha\seleium\chromedriver.exe")
def get_driver():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    element = float(text.split(":")[1])
    return element

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())
