from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.common.action_chains import ActionChains
import keyboard

class item:

    #Class constructor.    
    def __init__(self, name_id, price_id, owned_id):
        #Name takes the same value.
        self.name = driver.find_element_by_id(name_id).text     
        
        #Make the price id equal to the string for obtaining the price of the item.
        self.price_id = price_id

        #Owned_id will be used to confidently know how many buildings where already buyed
        self.owned_id = owned_id

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

    #Function used to update the number of buildings owned.
    def update_owned(self):
        if(self.owned > 0):
            self.owned = int(driver.find_element_by_id(self.owned_id).text)
        elif(self.owned == 0):
            self.owned += 1
    
    #Function used to buy an item, update price, number of items owned, and print the info about the item.
    def buy_action(self):
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(driver.find_element_by_id(self.price_id))
        upgrade_actions.click()
        upgrade_actions.perform()
        self.update_owned()
        self.update_price()
        self.print_info()

    #Fuction called when printing the info of an item.
    def print_info(self):
        print(f"Name: {self.name} \nPrice: {self.price}\nOwned: {self.owned}\n-----------------")

class upgrade:
    def __init__(self, id):
        self.id = id
        self.buyed = False
        self.can_buy = False

    def update_can_buy(self):
        driver.execute_script("console.log(Game.UpgradesById[" + str(self.id) + "].canBuy())")
        text = driver.get_log('browser')[0]
        text = text['message'].split(' ')[2]
        if(text == 'true'):
            self.can_buy = True
        else:
            self.can_buy = False

    def buy_upgrade(self):
        driver.execute_script("Game.UpgradesById[" + str(self.id) + "].click(event)")
        self.buyed = True
        print('Upgrade Buyed\n--------------------------------------')

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

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'browser': 'ALL'}

driver = webdriver.Chrome(desired_capabilities=d)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click(cookie)

#List of usable upgrades
usable_upgrades = [0,1,2,3,4,5,6,43,82,109,188,189,660,7,8,9,44,110,192,294,307,428,480,506,662,700,10,11,12,45,111,193,295,308,429,481,507,663,701,16,17,18,47,113,195,296,309,430,482,508,664,702,13,14,15,46,112,194,297,310,431,483,509,665,703,232,233,234,235,236,237,298,311,432,484,510,666,704,238,239,240,241,242,243,299,312,433,485,511,667,705,244,245,246,247,248,249,300,313,434,486,512,668,706,19,20,21,48,114,196,301,314,435,487,513,669,707,22,23,24,49,115,197,302,315,436,488,514,670,708,25,26,27,50,115,198,303,316,437,489,515,671,709,28,29,30,51,117,199,304,317,438,490,516,672,710,99,100,101,102,118,200,305,318,439,491,517,673,711,175,176,177,178,179,201,306,319,440,492,518,674,712,416,417,418,419,420,421,422,423,441,493,519,675,713,522,523,524,525,526,527,528,529,530,531,532,676,714,594,595,596,597,598,599,600,601,602,603,604,677,715,683,685,686,687,688,689,690,691,692,693,694,695,716,57,58,59,250,251,252,60,61,62,63,103,180,415,521,593,684,31,32,54,108,187,320,321,322,425,442,462,494,613,75,76,77,78,119,190,191,366,367,427,460,461,661,33,34,35,36,37,502,503,504,727,38,728,39,40,41,42,55,56,80,81,88,89,90,92,104,105,106,107,150,151,256,257,258,259]
usable_upgrades.sort()

#Get size of the upgrades list.
index_upgrades = len(usable_upgrades)

#Define step so program doesn't loop trhough all upgrades at once
index_step = 2
step = 18

upgrades = [] #List for storing upgrade objects.
items = [] #list for storing the item objects.
flags = [] #Flags to control when to add a new object.
for i in range(18): #Give all atributes a value of false.
    flags.append(False) 
initial_price = [15, 100, 1100, 12000, 130000, 1400000, 20000000, 330000000, 5100000000, 75000000000, 1000000000000, 14000000000000, 170000000000000, 2100000000000000, 26000000000000000, 310000000000000000, 71000000000000000000, 12000000000000000000000] #Initial values of the different buildings.
item_cap = 10 #Maximum quantity of items the program should buy, it changes through time.

#Initializing upgrades objects
for i in range(index_upgrades):
    upgrades.append(upgrade(usable_upgrades[i]))

#Flush console logs.
driver.get_log('browser')

#Main program.
while True:
    if(keyboard.is_pressed("3")):
        print("Finishing the program")
        break
    else:
        for i in range(40):
            actions.perform()

        for i in range(index_step):
            if(not(upgrades[i].buyed)):
                upgrades[i].update_can_buy()
                if(upgrades[i].can_buy):
                    upgrades[i].buy_upgrade()

        count = get_cookie_num(cookie_count.text)

        for i in range(18):
            if(count > initial_price[i] and not(flags[i])):
                items.append(item(("productName" + str(i)),("productPrice" + str(i)), ("productOwned" + str(i))))
                print(f"{items[i].name} appended\n-------------")
                flags[i] = True
                item_cap += 5
                print("Item Cap increased by: 5\n-------------")
                if(i > 0):
                    index_step += step
                    print("Upgrade search expanded\n--------------------")

        for i in range(17, -1 , -1):
            if(flags[i] and count > items[i].price and item_cap > items[i].owned):
                items[i].buy_action()
                if(item_cap == items[i].owned):
                    print("Item Capped\n---------------")
                count = get_cookie_num(cookie_count.text)
                

