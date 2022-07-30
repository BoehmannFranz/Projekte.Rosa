import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#config and init chromedriver 
options = webdriver.ChromeOptions() 
options.add_argument("--incognito")

# start webdriver
driver = webdriver.Chrome(options=options)

# paste url
driver.get("https://www.google.com/search?q=youtube+.boehmann+leuchten&oq=youtube+.boehmann+leuchten&aqs=chrome..69i57j69i64.9854j0j7&sourceid=chrome&ie=UTF-8#:~:text=.Boehmann%20%2D%20Leuchten%20%5BGlow,com%20%E2%80%BA%20watch")

#
# 1) Selenium zum laufen kriegen
# 2) Base nicht als hauptvariable entfernen
# 3) Grundfunktionen schreiben 