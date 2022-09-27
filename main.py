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
        url = "https://www.3djuegos.com/top-100/ps4/"
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.maximize_window()
        browser.get(url)
        for i in range(1,100):
            gameXpath = '//*[@id="tb926"]/div[1]/div[6]/div[1]/table[2]/tbody/tr['+str(i)+']/td[3]/a'
            gameElement = browser.find_element(By.XPATH,gameXpath)
            gameName = gameElement.get_attribute("innerHTML")
            print(gameName)


    def gameAmazon(self, name):
        games = []
        url = "https://www.amazon.com/s?k=" + name
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.maximize_window()
        browser.get(url)
        gameXPath = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img'
        gameTitleElement = browser.find_element(By.XPATH, gameXPath)
        gameTitleElement.click()
        gamePriceXpath = '//*[@id="priceblock_ourprice"]'
        gamePriceElement = browser.find_element(By.XPATH, gamePriceXpath)
        gamePriceText = gamePriceElement.get_attribute("innerHTML")
        print(gamePriceText)
        browser.get(url)

    def gameMetaCritic(self, name):
        games = []
        url1 = "https://www.metacritic.com/search/all/" + name +"/results"
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.maximize_window()
        browser.get(url1)
        metaGameXpath = '//*[@id="main_content"]/div/div[3]/div/ul/li[1]/div/div[2]/div/h3/a'
        metaGameElement = browser.find_element(By.XPATH, metaGameXpath)
        metaGameElement.click()
        metaScoreXPath = '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div/a/div/span'
        metaScoreElement = browser.find_element(By.XPATH, metaScoreXPath)
        metaScoreText = metaScoreElement.get_attribute("innerHTML")
        print(metaScoreText)
        


fetcher = scrapper()
#fetcher.gameAmazon("last of us")
#fetcher.searchTopGames()
fetcher.gameMetaCritic("last of us")

