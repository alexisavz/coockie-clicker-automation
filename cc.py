from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui, keyboard

class item:
    
    def __init__(self, name, price):
        self.name = name    #Name takes the same value. 

        #Check for prefixes after the price and adjust accordingly.
        if (price.find(" ") != -1):
            self.price = int(price.split(" ")[0]) * 1000000
        else:
            self.price = int(price)

        #convert string into integer.
        self.owned = 0

    def update_price(self, price):
        #Check for prefixes after the price and adjust accordingly.
        if (price.find(" ") != -1):
            self.price = int(price.split(" ")[0]) * 1000000
        else:
            self.price = int(price)

    def update_owned(self):
        self.owned +=1

    def buy_action(self, price):
        self.update_owned()
        self.update_price(price)
    
    def print_info(self):
        print(f"Name: {self.name} \nPrice: {self.price}\nOwned: {self.owned}")

def click_bunch():
    pyautogui.moveTo(285,465)
    pyautogui.click(clicks = 1000, interval = 0.0015)


driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click(cookie)

for i in range(25):
    actions.perform()

cursor = item(driver.find_element_by_id("productName0").text, driver.find_element_by_id("productPrice0").text)


while True:
    if(keyboard.is_pressed("p")):
        print("Finishing the program")
        break
    else:
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        if(count > cursor.price):
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(driver.find_element_by_id("productName0"))
            upgrade_actions.click()
            upgrade_actions.perform()
            cursor.buy_action(driver.find_element_by_id("productPrice0").text)
            cursor.print_info()













