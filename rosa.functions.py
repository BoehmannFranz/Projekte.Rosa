import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#config and init chromedriver 
options = webdriver.ChromeOptions() 
options.add_argument("--incognito")

# start webdriver 
driver = webdriver.Chrome(options=options)
# # paste url
driver.get("www.google.com/search?q=youtube+.boehmann+leuchten&oq=youtube+.boehmann+leuchten&aqs=chrome..69i57j69i64.9854j0j7&sourceid=chrome&ie=UTF-8#:~:text=.Boehmann%20%2D%20Leuchten%20%5BGlow,com%20%E2%80%BA%20watch")
print(driver.title)

#
# 1) Selenium zum laufen kriegen (Chromedriver zum laufen kreigen --> path angeben wegen macos)
# 2) Base nicht als hauptvariable entfernen (done)
# 3) docker zum laufen kriegen (done)
# 3) Grundfunktionen schreiben 