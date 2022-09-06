# SELENIUM
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# get the webdriver
browserDriver = Firefox()
browserDriver.maximize_window()

# go to website
browserDriver.get('https://www.webgamesonline.com/towers-of-hanoi/')

# define the needed pieces
Stick1 = browserDriver.find_element(By.CSS_SELECTOR, "div#c51.c2")
Stick2 = browserDriver.find_element(By.CSS_SELECTOR, "div#c52.c2")
Stick3 = browserDriver.find_element(By.CSS_SELECTOR, "div#c53.c2")
Ring1 = browserDriver.find_element(By.CSS_SELECTOR, "div#I1.a2.b2")
Ring2 = browserDriver.find_element(By.CSS_SELECTOR, "div#I2.a2.b2")
Ring3 = browserDriver.find_element(By.CSS_SELECTOR, "div#I3.a2.b2")
Ring4 = browserDriver.find_element(By.CSS_SELECTOR, "div#I4.a2.b2")
Ring5 = browserDriver.find_element(By.CSS_SELECTOR, "div#I5.a2.b2")
Ring6 = browserDriver.find_element(By.CSS_SELECTOR, "div#I6.a2.b2")
Ring7 = browserDriver.find_element(By.CSS_SELECTOR, "div#I7.a2.b2")
Ring8 = browserDriver.find_element(By.CSS_SELECTOR, "div#I8.a2.b2")
Ring9 = browserDriver.find_element(By.CSS_SELECTOR, "div#I9.a2.b2")
