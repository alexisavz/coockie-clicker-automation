from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui, keyboard

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

for i in range(25):
    actions.perform()

items = []

items.append(item("productName0", "productPrice0"))

grandma_flag = False
farm_flag = False
mine_flag = False
factory_flag = False
bank_flag = False
temple_flag = False
wizard_tower_flag = False
shipment_flag = False
alchemy_lab_flag = False
portal_flag = False
time_machine_flag = False
antimatter_condenser_flag = False
prism_flag = False
chancemaker_flag= False
fractal_engine_flag = False
javascript_console_flag = False
idleverse_flag = False


item_cap = 15


while True:
    if(keyboard.is_pressed("p")):
        print("Finishing the program")
        break
    else:
        actions.perform()
        count = get_cookie_num(cookie_count.text)
        if(count > 100 and not(grandma_flag)):
            items.append(item("productName1", "productPrice1"))
            print(f"{items[1].name} appended")
            grandma_flag = True
        if(count > 1100 and not(farm_flag)):
            items.append(item("productName2", "productPrice2"))
            print(f"{items[2].name} appended")
            farm_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 12000 and not(mine_flag)):
            items.append(item("productName3", "productPrice3"))
            print(f"{items[3].name} appended")
            mine_flag = True
        if(count > 130000 and not(factory_flag)):
            items.append(item("productName4", "productPrice4"))
            print(f"{items[4].name} appended")
            factory_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 1400000 and not(bank_flag)):
            items.append(item("productName5", "productPrice5"))
            print(f"{items[5].name} appended")
            bank_flag = True
        if(count > 20000000 and not(temple_flag)):
            items.append(item("productName6", "productPrice6"))
            print(f"{items[6].name} appended")
            temple_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 330000000 and not(wizard_tower_flag)):
            items.append(item("productName7", "productPrice7"))
            print(f"{items[7].name} appended")
            wizard_tower_flag = True
        if(count > 5100000000 and not(shipment_flag)):
            items.append(item("productName8", "productPrice8"))
            print(f"{items[8].name} appended")
            shipment_flag = True
        if(count > 75000000000 and not(alchemy_lab_flag)):
            items.append(item("productName9", "productPrice9"))
            print(f"{items[9].name} appended")
            alchemy_lab_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 1000000000000 and not(portal_flag)):
            items.append(item("productName10","productPrice10"))
            print(f"{items[10].name} appended")
            portal_flag = True
        if(count > 14000000000000 and not(time_machine_flag)):
            items.append(item("productName11", "productPrice11"))
            print(f"{items[11].name} append")
            time_machine_flag = True
        if(count > 170000000000000 and not(antimatter_condenser_flag)):
            items.append(item("productName12", "productPrice12"))
            print(f"{items[12].name} appended")
            antimatter_condenser_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 2100000000000000 and not(prism_flag)):
            items.append(item("productName13", "productPrice13"))
            print(f"{items[13].name} appended")
            prism_flag = True
        if(count > 26000000000000000 and not(chancemaker_flag)):
            items.append(item("productName14", "productPrice14"))
            print(f"{items[14].name} appended")
            chancemaker_flag = True
        if(count > 310000000000000000 and not(fractal_engine_flag)):
            items.append(item("productName15", "productPrice15"))
            print(f"{items[15].name} appended")
            fractal_engine_flag = True
            item_cap += 5
            print("Incremented Item Cap")
        if(count > 71000000000000000000 and not(javascript_console_flag)):
            items.append(item("productName16", "productPrice16"))
            print(f"{items[16].name} appended")
            javascript_console_flag = True
        if(count > 12000000000000000000000 and not(idleverse_flag)):
            items.append(item("productName17", "productPrice17"))
            print(f"{items[17].name} appended")
            prism_flag = True
            item_cap += 5
            print("Incremented Item Cap")

        if(idleverse_flag and count > items[17].price and item_cap > items[17].owned):
            items[17].buy_action()
        if(javascript_console_flag and count > items[16].price and item_cap > items[16].owned):
            items[16].buy_action()
        if(fractal_engine_flag and count > items[15].price and item_cap > items[15].owned):
            items[15].buy_action()
        if(chancemaker_flag and count > items[14].price and item_cap > items[14].owned):
            items[14].buy_action()
        if(prism_flag and count > items[13].price and item_cap > items[13].owned):
            items[13].buy_action()
        if(antimatter_condenser_flag and count > items[12].price and item_cap > items[12].owned):
            items[12].buy_action()
        if(time_machine_flag and count > items[11].price and item_cap > items[11].owned):
            items[11].buy_action()
        if(portal_flag and count > items[10].price and item_cap > items[10].owned):
            items[10].buy_action()
        if(alchemy_lab_flag and count > items[9].price and item_cap > items[9].owned):
            items[9].buy_actions()
        elif(shipment_flag and count > items[8].price and item_cap > items[8].owned):
            items[8].buy_action()
        elif(wizard_tower_flag and count > items[7].price and item_cap > items[7].owned):
            items[7].buy_action()
        elif(temple_flag and count > items[6].price and item_cap > items[6].owned):
            items[6].buy_action()
        elif(bank_flag and count > items[5].price and item_cap > items[5].owned):
            items[5].buy_action()
        elif(factory_flag and count > items[4].price and item_cap > items[4].owned):
            items[4].buy_action()
        elif(mine_flag and count > items[3].price and item_cap > items[3].owned):
            items[3].buy_action()
        elif(farm_flag and count > items[2].price and item_cap > items[2].owned):
            items[2].buy_action()
        elif(grandma_flag and count > items[1].price and item_cap > items[1].owned):
            items[1].buy_action()
        elif(count > items[0].price and item_cap > items[0].owned):
            items[0].buy_action()


