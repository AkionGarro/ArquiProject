from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import multiprocessing as mp
from joblib import Parallel,delayed
import csv


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
        games = []
        url = "https://www.3djuegos.com/top-100/ps4/"
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service,options=options)
        browser.get(url)
        for i in range(1,80):
            gameSelector = '#tb926 > div.izq2 > div.mar_t5.bgc0.br3.mar_rl3.s11.c7 > div.pad_rl8.fftext > table:nth-child(3) > tbody > tr:nth-child('+str(i)+') > td:nth-child(3) > a '
            gameElement = browser.find_element(By.CSS_SELECTOR,gameSelector)
            gameName = gameElement.get_attribute("innerHTML")
            games.append(gameName)
            print(gameName)
        browser.close()
        return games

    def gameAmazon(self, game):
            service = Service(verbose=True)
            options = Options()
            options.add_argument("headless")
            browser = webdriver.Edge(service=service, options=options)
            try:
                url = "https://www.amazon.com/s?k=" + game +" PlayStation 4 Game"
                browser.get(url)
                gameTitleElement = browser.find_element(By.CSS_SELECTOR,'img.s-image')
                gameTitleElement.click()
                gamePriceID = 'priceblock_ourprice'
                gamePriceElement = browser.find_element(By.ID, gamePriceID)
                gamePriceText = gamePriceElement.get_attribute("innerHTML")
                print(gamePriceText)
                return gamePriceText
            except:
                print("error")
            browser.close()



    def gameMetaCritic(self, name):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        try:
            url = "https://www.metacritic.com/search/all/" + name + "/results"
            browser.get(url)
            metaGameXpath = '//*[@id="main_content"]/div/div[3]/div/ul/li[1]/div/div[2]/div/span'
            metaGameElement = browser.find_element(By.XPATH, metaGameXpath)
            metaScoreText = metaGameElement.get_attribute("innerHTML")
            print(metaScoreText)
            return metaScoreText
        except:
            print("error")
            return "invalid"
        browser.close()



    def gameHowLongToBeat(self,name):

        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        try:
            url = "https://howlongtobeat.com/?q="+name
            browser.get(url)
            timeGameXpath = '//*[@id="search-results-header"]/ul/li[1]/div[2]/div/div/div[2]'
            timeGameElement = browser.find_element(By.XPATH, timeGameXpath)
            timeGameText = timeGameElement.get_attribute("innerHTML");
            print(timeGameText)
            return timeGameText
        except:
            print("error")
            return "invalid"
        browser.close()








fetcher = scrapper()
games = []
with open('games.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        games.append(row[0])
for i in games:
    print(i)
#Parallel way
num_cores = mp.cpu_count()
amazonPrices = Parallel(mp.cpu_count())(delayed(fetcher.gameAmazon)(i) for i in games)
metaScore = Parallel(mp.cpu_count())(delayed(fetcher.gameMetaCritic)(i) for i in games)
metaScore = Parallel(mp.cpu_count())(delayed(fetcher.gameHowLongToBeat)(i) for i in games)