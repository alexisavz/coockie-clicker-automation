from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import keyboard

class item:

    #Class constructor.    
    def __init__(self, name_id, price_id):
        self.name = driver.find_element_by_id(name_id).text    #Name takes the same value. 
        
        #Make the price id equal to the string for obtaining the price of the item.
        self.price_id = price_id

        #Check for prefixes after the price and adjust accordingly.
        text = driver.find_element_by_id(self.price_id).text
        if(text.find(' ') == -1):
            if(text.find(',') == -1):
                self.price = int(text)
            else:
                self.price = int(text.replace(',',''))
        else:
            if(text.split(' ')[1] == 'million'):
                self.price = int(float(text.split[0]) * 1000000)
            if(text.split(' ')[1] == 'billion'):
                self.price = int(float(text.split[0]) * 1000000000)
            if(text.split(' ')[1] == 'trillion'):
                self.price = int(float(text.split[0]) * 1000000000000)
            if(text.split(' ')[1] == 'quadrillion'):
                self.price = int(float(text.split[0]) * 1000000000000000)
            if(text.split(' ')[1] == 'quintillion'):
                self.price = int(float(text.split[0]) * 1000000000000000000)
            if(text.split(' ')[1] == 'sextillion'):
                self.price = int(float(text.split[0]) * 1000000000000000000000)   

        #convert string into integer.
        self.owned = 0

    #Function used to update the price sotred for each item.
    def update_price(self):
        #Check for prefixes after the price and adjust accordingly.
        text = driver.find_element_by_id(self.price_id).text
        if(text.find(' ') == -1):
            if(text.find(',') == -1):
                self.price = int(text)
            else:
                self.price = int(text.replace(',',''))
        else:
            if(text.split(' ')[1] == 'million'):
                self.price = int(float(text.split()[0]) * 1000000)
            if(text.split(' ')[1] == 'billion'):
                self.price = int(float(text.split()[0]) * 1000000000)
            if(text.split(' ')[1] == 'trillion'):
                self.price = int(float(text.split()[0]) * 1000000000000)
            if(text.split(' ')[1] == 'quadrillion'):
                self.price = int(float(text.split()[0]) * 1000000000000000)
            if(text.split(' ')[1] == 'quintillion'):
                self.price = int(float(text.split()[0]) * 1000000000000000000)
            if(text.split(' ')[1] == 'sextillion'):
                self.price = int(float(text.split()[0]) * 1000000000000000000000)                

    #Function used to buy an item, update price, number of items owned, and print the info about the item.
    def buy_action(self):
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(driver.find_element_by_id(self.price_id))
        upgrade_actions.click()
        upgrade_actions.perform()
        self.owned += 1
        self.update_price()
        self.print_info()

    #Fuction called when printing the info of an item.
    def print_info(self):
        print(f"Name: {self.name} \nPrice: {self.price}\nOwned: {self.owned}\n-----------------")

#Function used to convert cookie number string to a usable integer.
def get_cookie_num(text):
    num = None
    string = text.split()
    if(string[1] == 'cookies'):
        if(string[0].find(',') == -1):
            num = int(string[0])
        else:
            num = int(string[0].replace(',', ''))
    if(string[1] == 'million'):
        num = int(float(string[0]) * 1000000)
    if(string[1] == 'billion'):
        num = int(float(string[0]) * 1000000000)
    if(string[1] == 'trillion'):
        num = int(float(string[0]) * 1000000000000)    
    if(string[1] == 'quadrillion'):
        num = int(float(string[0]) * 1000000000000000)
    if(string[1] == 'quintillion'):
        num = int(float(string[0]) * 1000000000000000000)
    if(string[1] == 'sextillion'):
        num = int(float(string[0]) * 1000000000000000000000)
    return num

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click(cookie)

items = [] #list for storing the item objects.
flags = [] #Flags to control when to add a new object.
for i in range(18): #Give all atributes a value of false.
    flags.append(False) 
initial_price = [15, 100, 1100, 12000, 130000, 1400000, 20000000, 330000000, 5100000000, 75000000000, 1000000000000, 14000000000000, 170000000000000, 2100000000000000, 26000000000000000, 310000000000000000, 71000000000000000000, 12000000000000000000000] #Initial values of the different buildings.
item_cap = 15 #Maximum quantity of items the program should buy, it changes through time.

#Clicks necessary to unlock the first item.
for i in range(15):
    actions.perform()

#Main program.
while True:
    if(keyboard.is_pressed("p")):
        print("Finishing the program")
        break
    else:
        actions.perform()
        count = get_cookie_num(cookie_count.text)
        for i in range(18):
            if(count > initial_price[i] and not(flags[i])):
                items.append(item(("productName" + str(i)),("productPrice" + str(i))))
                print(f"{items[i].name} appended\n-------------")
                flags[i] = True
                item_cap += 2
                print("Item Cap increased by: 2\n-------------")
        
        for i in range(17, -1 , -1):
            if(flags[i] and count > items[i].price and item_cap > items[i].owned):
                items[i].buy_action()
                if(item_cap == items[i].owned):
                    print("Item Capped\n---------------")
    

