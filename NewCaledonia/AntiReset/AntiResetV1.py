from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.by import By
import time
import random

browser=webdriver.Chrome()
browser.get("https://m-ums.opt.nc/index.php")

name = input("Escribe numero de telefono: ")
name2 = input("Escriba la clave del telefono: ")

element=browser.find_element(By.ID,"login")
element.send_keys(name)
element=browser.find_element(By.ID,"password")
element.send_keys(name2)
element.submit()
time.sleep(4)
element=browser.find_element(By.XPATH,'//*[@title="PIN"]').click()
time.sleep(3)

i = 0
while i < 1000000:
    newi = "{:04d}".format(random.randint(0, 9999))
    password = '' + str(newi)
    element=browser.find_element(By.XPATH, '//*[@name="newpin"]')
    element.send_keys(newi)
    element=browser.find_element(By.XPATH, '//*[@name="newpin2"]')
    element.send_keys(newi)
    print(newi)
    element.submit()
    time.sleep(5)
    print(browser.current_url)
    browser.get(browser.current_url)
    time.sleep(3)
    i += 1

print("Success")
