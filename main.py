# import namespaces to operate driver and selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# cache a path to the driver executable to make calls on chrome browser
PATH = "C:\chromedriver_win32\chromedriver.exe";
driver = webdriver.Chrome(service=Service(PATH));

# get the webpage we want to visit and print title to log
driver.get("https://austin.craigslist.org/location/austin-tx?lat=30.2509&lon=-97.742&search_distance=13");
print(driver.title);

# call function to find the HTML element by its ID name
search = driver.find_element(by=By.ID, value="query");

# send the information to the webpage for what we want to search
search.send_keys("apartments");

# execute the search
search.send_keys(Keys.RETURN);

# page is loaded, locate the class that controls price min max
search = driver.find_element(by=By.CLASS_NAME, value="range-inputs");

# cache the input in a list because they do not have unique identifiers
s_list = search.find_elements(by=By.TAG_NAME, value="input");

# send prices to each element of the last and tell browser to execute search
s_list[0].send_keys("800");
s_list[1].send_keys("1200");
s_list[1].send_keys(Keys.RETURN);

# Browser now shows all apartments in Austin tx between 800-1200 dollars

# store search results into a list
results = driver.find_element(By.ID, value="search-results")
l_results = results.find_elements(by=By.CLASS_NAME, value="result-row")

# establish a path for a text file
file_path = os.path.abspath(r'C:\Users\12624\Desktop\clapartments')
text_file = open("cl_apartments", "w")

# iterate thru list and print text to text file
try:

    for result in l_results:
        text = result.get_attribute("textContent")
        text_file = open("cl_apartments", "a")
        text_file.write(text)

except:
    pass

# some unicode errors were raising exceptions, using pass lead to usable results

