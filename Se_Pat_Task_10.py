from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
import time
#from Selenium import driver

# service_obj = Service("C:/Users/dell/PycharmProjects/driver/chromedriver.exe") # with chromedriver
#driver.get("https://www.google.com/") # to open specified url in the browser & navigate to the given webpage

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome() # with the WebDriver corresponding to your browser

# Open the target website (e.g., Instagram)
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
time.sleep(5)

#login to the website
# username = driver.find_element(By.ID, 'username-field')
# password = driver.find_element(By.XPATH, ("//input[@id='password-field']"))

# #set the credential to login the page.
# username.send_keys("a&%%$")
# password.send_keys("*****")

#this type is not working need to check that.
#get_followers = driver.find_element(By.XPATH, ("//span[@class = 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']"))

get_followers = driver.find_element(By.XPATH, "//*[contains(text(), 'followers')]").text
time.sleep(5)

get_following = driver.find_element(By.XPATH, "//*[contains(text(), 'following')]").text
time.sleep(5)

# Print the list of followers
print(get_followers)
print(get_following)