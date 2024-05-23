# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:30:26 2024

@author: NjeriWanjiru
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#set up chrome driver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://google.com")

#search for elements in htmlz; type an item and get results upon clicking enter
WebDriverWait(driver, 5).until(EC.presence_of_element_located((
    By.CLASS_NAME, "gLFyf")))

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys('Best Data Science Tutorials' +  Keys.ENTER)

#find an element based on the text
WebDriverWait(driver, 5).until(EC.presence_of_element_located((
    By.PARTIAL_LINK_TEXT, 'Best Data Science Tutorials')))

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Best Data Science Tutorials')
link.click()


time.sleep(10)

driver.quit()