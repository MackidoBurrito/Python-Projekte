import time

# SELENIUM
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # get the webdriver
    driver = Firefox()
    driver.maximize_window()
    # website is entered
    driver.get('https://www.wetteronline.de/')
    # accept cookies
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sp_message_iframe_585821")))
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.message-component.message-button.no-children.focusable.close.sp_choice_type_11.first-focusable-el"))).click()
    driver.switch_to.default_content()
    # searchbar
    searchbar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#searchstring")))
    searchbar.click()
    searchbar.send_keys("Herford")
    searchbar.submit()
    time.sleep(10)
    driver.close()


def main2():
    # get the webdriver
    driver = Firefox()
    driver.maximize_window()
    # website is entered
    driver.get('https://www.wetter.de/')
    # accept cookies
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sp_message_iframe_696049")))
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.message-component.message-button.no-children.focusable.sp_choice_type_11"))).click()
    driver.switch_to.default_content()
    # searchbar
    searchbar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input")))
    searchbar.click()
    searchbar.send_keys("Herford")
    time.sleep(1)
    searchbar.send_keys(Keys.ENTER)
    time.sleep(10)
    driver.close()

if __name__ == '__main__':
    for i in range(100):
        main()
        main2()
