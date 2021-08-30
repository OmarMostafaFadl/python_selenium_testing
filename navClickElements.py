from selenium import webdriver
from selenium.webdriver.common.keys import Keys      #Allows us to use Enter, ESC, Space...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"     #Setting up the path for the chrome driver
driver = webdriver.Chrome(PATH)                      #Setting up the webdriver as chrome

driver.get("https://www.techwithtim.net")            #Opening a website

link = driver.find_element_by_link_text("Python Programming")   #Finds the Element by its visuaized name on the webpage
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))    #Clicks on Beginner Python Tutorials Element 
    )
    element.click()

    driver.back()              #Goes back to the last webpage
    driver.back()
    #driver.forward()           #Goes Forward

except:
    driver.quit()

time.sleep(2)

driver.quit()


