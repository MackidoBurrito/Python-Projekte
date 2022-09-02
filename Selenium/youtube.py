# BUILTIN
import time

# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # get the webdriver
    browserDriver = Firefox()
    browserDriver.maximize_window()

    # go to youtube
    browserDriver.get('https://www.youtube.com')
    # accept cookies
    cookies = WebDriverWait(browserDriver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Accept the use of cookies and other data for the purposes described"]')))
    #browserDriver.implicitly_wait(10)
    #cookies = browserDriver (driver, 10)
    #cookies = browserDriver.find_element(By.CSS_SELECTOR, '[aria-label="Accept the use of cookies and other data for the purposes described"]')
    cookies.click()
    # searching
    #searchbar = WebDriverWait(browserDriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#search")))
    browserDriver.implicitly_wait(20)
    time.sleep(1)
    searchbar = browserDriver.find_element(By.CSS_SELECTOR, "input#search")
    searchbar.click()
    #browserDriver.implicitly_wait(10)
    searchbar.send_keys("Rick Astley Never gonna give you up")
    searchbar.submit()
    # click on video
    #browserDriver.implicitly_wait(10)
    videoselection = WebDriverWait(browserDriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#title-wrapper")))
    videoselection.click()
    # fullscreen
    #browserDriver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(browserDriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.ytp-fullscreen-button.ytp-button"))).click()
    #click_fullscreen.click()
    #time.sleep(1)
    #browserDriver.find_element(By.CSS_SELECTOR, "button.ytp-fullscreen-button.ytp-button").click()
    time.sleep(5)
    print("Moin")
    browserDriver.close()


if __name__ == '__main__':
    for i in range(100):
        main()
