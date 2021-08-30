from selenium import webdriver
from selenium.webdriver.common.keys import Keys      #Allows us to use Enter, ESC, Space...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"     #Setting up the path for the chrome driver
driver = webdriver.Chrome(PATH)                      #Setting up the webdriver as chrome



driver.get("https://www.techwithtim.net")            #Opening a website
title = driver.title             #Gets the webpage title


search = driver.find_element_by_name("s")        #finds an element in the source code by name s = search box
search.clear()
search.send_keys("test")                         #Types test in the search bar
search.send_keys(Keys.RETURN)                    #Presses ENTER


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))     #Tries for 10 seconds to fetch main from the source code.
    )
    #print(main.text)

    articles = main.find_elements_by_tag_name("article")

    for article in articles:
        header = article.find_element_by_class_name("entry-summary")    #getting all entry-summaries from the article found in the search
        print(header.text)

except:
    driver.quit()

driver.quit()





