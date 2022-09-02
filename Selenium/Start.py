# BUILTIN
import time

# SELENIUM
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox


def main():
    # get the webdriver
    browserDriver = Firefox()

    # go to google
    browserDriver.get('https://www.google.de')

    # accept cookies
    time.sleep(3)
    browserDriver.find_element(By.ID, "L2AGLb").click()

    # find the Search Input Element
    inputSearch = browserDriver.find_element(By.NAME, "q")
    # type "do a barrel role"
    time.sleep(1)
    inputSearch.send_keys("do a barrel roll")
    # start the search by submitting the input
    inputSearch.submit()


if __name__ == '__main__':
    main()
