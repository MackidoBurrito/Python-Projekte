# SELENIUM
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def main():
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
    # move the pieces
    ActionChains(browserDriver).drag_and_drop(Ring1, Stick3).perform()
    ActionChains(browserDriver).drag_and_drop(Ring2, Stick2).perform()
    ActionChains(browserDriver).drag_and_drop(Ring1, Stick2).perform()
    ActionChains(browserDriver).drag_and_drop(Ring3, Stick3).perform()
    ActionChains(browserDriver).drag_and_drop(Ring1, Stick1).perform()
    ActionChains(browserDriver).drag_and_drop(Ring2, Stick3).perform()
    ActionChains(browserDriver).drag_and_drop(Ring1, Stick3).perform()
    time.sleep(2)
    browserDriver.close()

if __name__ == '__main__':
    for i in range(100):
        main()
