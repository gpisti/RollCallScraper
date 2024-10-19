from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def initialize_web_driver():
    """Initializing a WebDriver using Brave browser"""
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" # <-- MÁS GÉP ESETÉN ÁTÍRANDÓ ADOTT ELÉRÉSI ÚTVONALRA
    #Támogat minden Chromium alapú böngészőt! (A változó azért van így elnevezve, mert én Brave Browser-t használtam)
    chrome_options = Options()
    chrome_options.binary_location = brave_path

    chrome_driver_path = "D:\\Prog\\Chromium\\chromedriver-win64\\chromedriver.exe" # <-- MÁS GÉP ESETÉN ÁTÍRANDÓ ADOTT ELÉRÉSI ÚTVONALÁRA
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.senate.gov/legislative/votes_new.htm")

    return driver
