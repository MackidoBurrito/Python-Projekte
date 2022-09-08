# SELENIUM
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# navigate to website and to the right ring amount
def main():
    ring_amount = input("Wie viele Ringe(3 - 9): ")
    if not ring_amount.isnumeric():
        print("Bitte eine  Zahl zwischen 3 und 9 eingeben")
        exit()
    if ring_amount < "3" or ring_amount > "9":
        print("Bitte eine  Zahl zwischen 3 und 9 eingeben")
        exit()
    wd = Firefox()
    wd.maximize_window()
    wd.get('https://www.webgamesonline.com/towers-of-hanoi/')
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select"))).click()
    if ring_amount == "3":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="7"]'))).click()
    elif ring_amount == "4":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="15"]'))).click()
    elif ring_amount == "5":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="31"]'))).click()
    elif ring_amount == "6":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="63"]'))).click()
    elif ring_amount == "7":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="127"]'))).click()
    elif ring_amount == "8":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="255"]'))).click()
    elif ring_amount == "9":
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="511"]'))).click()
    #define rings and sticks
    Stick1 = wd.find_element(By.CSS_SELECTOR, "div#c51.c2")
    Stick2 = wd.find_element(By.CSS_SELECTOR, "div#c52.c2")
    Stick3 = wd.find_element(By.CSS_SELECTOR, "div#c53.c2")
    Ring1 = wd.find_element(By.CSS_SELECTOR, "div#I1.a2.b2")
    Ring2 = wd.find_element(By.CSS_SELECTOR, "div#I2.a2.b2")
    Ring3 = wd.find_element(By.CSS_SELECTOR, "div#I3.a2.b2")
    Ring4 = wd.find_element(By.CSS_SELECTOR, "div#I4.a2.b2")
    Ring5 = wd.find_element(By.CSS_SELECTOR, "div#I5.a2.b2")
    Ring6 = wd.find_element(By.CSS_SELECTOR, "div#I6.a2.b2")
    Ring7 = wd.find_element(By.CSS_SELECTOR, "div#I7.a2.b2")
    Ring8 = wd.find_element(By.CSS_SELECTOR, "div#I8.a2.b2")
    Ring9 = wd.find_element(By.CSS_SELECTOR, "div#I9.a2.b2")
    Stick1_list = {
        1: Ring1,
        2: Ring2,
        3: Ring3,
        4: Ring4,
        5: Ring5,
        6: Ring6,
        7: Ring7,
        8: Ring8,
        9: Ring9,
    }
    Stick2_list = {
    }
    Stick3_list = {
    }

    # function for moving the rings
    def solving():
        while True:
            end = wd.find_elements(By.CSS_SELECTOR, '[style="background-color: transparent;"]')
            endlist = len(end)
            if endlist > 0:
                print("JUHU")
                break
            elif len(Stick3_list) <= 0:
                print("AAAAA")
                # moveable_ring = Stick1_list.get[1]
                # print(moveable_ring)
                ActionChains(wd).drag_and_drop(Stick1_list[0], Stick3).perform()
                Stick3_list.insert(0, Stick1_list[0])
                Stick1_list.pop()[0]
            elif Stick1_list[0] < Stick3_list[0]:
                ActionChains(wd).drag_and_drop(Stick1_list[0], Stick3).perform()
                Stick3_list.insert(0, Stick1_list[0])
                Stick1_list.pop(0)
            elif Stick1_list[0] < Stick2_list[0]:
                ActionChains(wd).drag_and_drop(Stick1_list[0], Stick2).perform()
                Stick3_list.insert(0, Stick1_list[0])
                Stick1_list.pop(0)
            # ActionChains(browserDriver).drag_and_drop(Stick1_list, Stick3).perform()
            Stick3_list.insert(0, Stick1_list[0])
            Stick1_list.pop(0)
            print(Stick3_list)
            print(Stick1_list)
    solving()


if __name__ == "__main__":
    main()
