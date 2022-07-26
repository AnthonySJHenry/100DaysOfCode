from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.remote.webelement import WebElement

#A demo that just pulls up flask's jinja page on wikipedia

chrome_driver_path = "/Users/ah/Desktop/100DaysOfCode/Web_Scraping/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.wikipedia.org/")
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python Flask")
search_box.send_keys(Keys.ENTER)

jinja_link = driver.find_element(By.LINK_TEXT, "Jinja")
jinja_link.click()

driver.quit()