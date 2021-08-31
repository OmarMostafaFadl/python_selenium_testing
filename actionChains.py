from selenium import webdriver
from selenium.webdriver.common.keys import Keys      #Allows us to use Enter, ESC, Space...
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"     #Setting up the path for the chrome driver
driver = webdriver.Chrome(PATH)                      #Setting up the webdriver as chrome

driver.get("https://orteil.dashnet.org/cookieclicker/")            #Opening a website

""" How to Use Actions: 

    - Create an action chain, which is the needed actions to work in a sequence
    - .perform() to perform all of those actions """

driver.implicitly_wait(5)            #waits 5 seconds

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(2)]

actions = ActionChains(driver)                        #Create an object of ActionChains that acts on driver
actions.click(cookie)

NUMBER_OF_CLICKS = 50


for i in range(NUMBER_OF_CLICKS):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.click(item)
            upgrade_actions.perform()


time.sleep(5)

driver.quit()
