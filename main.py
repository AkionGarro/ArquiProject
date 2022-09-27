import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class amazonGame():
    def __init__(self, title, price):
        self.title = title
        self.price = price

class playStationGame():
    def __init__(self, title, price):
        self.title = title
        self.price = price


class scrapper:

    def searchTopGames(self):
        url2 = "https://www.3djuegos.com/top-100/ps4/"
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.maximize_window()
        browser.get(url2)
        for i in range(1,100):
            itemPath = '//*[@id="tb926"]/div[1]/div[6]/div[1]/table[2]/tbody/tr['+str(i)+']/td[3]/a'
            element = browser.find_element(By.XPATH,itemPath)
            gameName = element.get_attribute("innerHTML")
            print(gameName)




fetcher = scrapper()
fetcher.game("last of us")
fetcher.searchTopGames()


