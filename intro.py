"""
Selenium is a tool for controlling a web browser through a program.
It was originally used for automation testers for web applications.
Selenium consist of the following components:
1 - Selenium IDE (Chrome Extension or Firefox Add-On)
2 - Selenium RC (Remote Control)
3 - Selenium Web Driver
4 - Selenium GRID
"""
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Will start the driver.
chromedriver = Service(f"driver/chromedriver.exe")
driver = webdriver.Chrome(service=chromedriver)

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.ID, 'gcse-form')

# create action chain
actions = ActionChains(driver)
actions.click(on_element=element)
actions.pause(0.2)
actions.send_keys_to_element(element, "123")
actions.send_keys_to_element(element, Keys.RETURN)
actions.perform()
