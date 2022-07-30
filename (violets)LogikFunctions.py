from http.client import ImproperConnectionState
from lib2to3.pgen2 import driver
import time
import accounts
import random
# from violetsLogikFunctions import uniqueDriverNames
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create amount of drivernames on the amount of streams
def uniqueDriverNames(streams):
    driverlist = []
    for i in range(streams):
        DriverName = 'driver'+str(i)
        driverlist.append(DriverName)
        i+= 1
    return driverlist



def VioletInAction(AccountID, streams, ArtistName, SongName, PlayTime):
    
    SearchWords = ArtistName + SongName
    Humanize = PlayTime/ 100 * random.randrange(3,18)
    HumanPlayTime = PlayTime + Humanize 
    iterator = 0
    # Streamdriver = uniqueDriverNames(AccountID)

    #config and init chromedriver 
    options = webdriver.ChromeOptions() 
    options.add_argument("--incognito")
    # options.add_argument("start-maximized")


    # while (iterator < streams):

    # start webdriver 
    driver = webdriver.Chrome(options=options)
    # # paste url
    driver.get("https://accounts.spotify.com/de/login")
    print(driver.title)

    #Login
    driver.find_element(By.XPATH, './/*[@id="login-username"]').send_keys(accounts.username[AccountID])
    time.sleep(0.1)
    driver.find_element(By.XPATH, './/*[@id="login-password"]').send_keys(accounts.password[AccountID])
    time.sleep(0.1)
    driver.find_element(By.XPATH, './/*[@id="login-button"]').click()

    # choose Webplayer button
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'.//*[@id="root"]/div/div[2]/div/div/button[2]'))).click()
    except:
        print("\n Abbruch - choose Webplayer")

    # Click Icon of searchbar
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'.//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]'))).click()
        time.sleep(0.5)
    except:
        print("\nerror - click icon of searchbar")

    # click into searchbar
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'.//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input'))).click()
        time.sleep(0.5)
    except:
        print("\nerror - click into searchbar")

    # SearchWords into searchbar
    try:
        driver.find_element (By.XPATH,'.//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input').send_keys(SearchWords)
        time.sleep(0.5)
    except:
        print("\n error - SearchWords into searchbar")

    # klick artist banner
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/*[@id="searchPage"]/div/div/section[1]/div[2]/div'))).click()
        time.sleep(0.5)
    except:
        print("\n error - artist banner")
        
    # klick first Song
    try:
        print('\nclick Song' )
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button'))).click()  
        time.sleep(0.5)
    except:
        print("\n error - click song")
    time.sleep(3)

    time.sleep(HumanPlayTime) 
   