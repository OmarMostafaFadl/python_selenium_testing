from selenium import webdriver
from selenium.webdriver.common.keys import Keys      #Allows us to use Enter, ESC, Space...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"     #Setting up the path for the chrome driver
driver = webdriver.Chrome(PATH)                      #Setting up the webdriver as chrome


driver.get("https://www.google.com")            #Opening a website
title = driver.title             #Gets the webpage title


search = driver.find_element_by_name("q")        #finds an element in the source code by name 
search.clear()
search.send_keys("Ronaldo")                         
search.send_keys(Keys.RETURN)                    #Presses ENTER


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "الطول")) 
    )
    element.click()
    time.sleep(2)
    driver.back()              #Goes back to the last webpage

except:
    driver.quit()

driver.quit()





