from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import multiprocessing as mp
from joblib import Parallel, delayed
import csv
import time

from DataBase import AzureConnection


class gameFull():
    def __init__(self, title, psPrice, amazonPrice, metaScore, howlong, imageLink):
        self.title = title
        self.psPrice = psPrice
        self.amazonPrice = amazonPrice
        self.metaScore = metaScore
        self.howlong = howlong
        self.imageLink = imageLink

    def printGameInfo(self):
        print("Name: " + self.title + "\n"
        "PlayStationPrice: " + self.psPrice + "\n"
        "AmazonPrice: " + self.amazonPrice + "\n"
        "Meta Score: " + self.metaScore + "\n"
        "How Long to Beat: " + self.howlong + "\n"
        "Enlace a imagen: " + self.imageLink + "\n")

class scrapper:

    def __init__(self):
        self.psPricesList = []
        self.amazonPricesList = []
        self.metaScoreList = []
        self.howLongList = []
        self.srcImagesList = []
        self.AllGamesList = []
        self.database = AzureConnection()

    def searchTopGames(self):
        games = []
        url = "https://www.3djuegos.com/top-100/ps4/"
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.get(url)
        for i in range(1, 80):
            gameSelector = '#tb926 > div.izq2 > div.mar_t5.bgc0.br3.mar_rl3.s11.c7 > div.pad_rl8.fftext > table:nth-child(3) > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > a '
            gameElement = browser.find_element(By.CSS_SELECTOR, gameSelector)
            gameName = gameElement.get_attribute("innerHTML")
            games.append(gameName)
        browser.close()
        return games

    def gamePlayStation(self, game):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.implicitly_wait(1)
        try:
            url = "https://store.playstation.com/es-cr/search/" + game
            browser.get(url)
            playGameXpath = '//*[@id="main"]/section/div/ul/li[1]/div/a/div/div'
            gameTitleElement = browser.find_element(By.XPATH, playGameXpath)
            gameTitleElement.click()
            gamePriceClass = 'psw-t-title-m'
            gamePriceElement = browser.find_element(By.CLASS_NAME, gamePriceClass)
            gamePriceText = gamePriceElement.get_attribute("innerHTML")
            if(str(gamePriceText) !="Gratuito"):
                self.psPricesList.append((str(gamePriceText[3:])))
            else:
                self.psPricesList.append(0)
        except:
            self.psPricesList.append(0)

        browser.close()

    def gameAmazon(self, game):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.implicitly_wait(1)
        try:
            url = "https://www.amazon.com/s?k=" + game + " ps4"
            browser.get(url)
            gameTitleElement = browser.find_element(By.CSS_SELECTOR, 'img.s-image')
            gameTitleElement.click()
            gamePriceID = 'priceblock_ourprice'
            gamePriceElement = browser.find_element(By.ID, gamePriceID)
            gamePriceText = gamePriceElement.get_attribute("innerHTML")
            self.amazonPricesList.append((str(gamePriceText[3:])))
        except:
            self.amazonPricesList.append(0)
        browser.close()

    def gameMetaCritic(self, name):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.implicitly_wait(2)
        try:
            url = "https://www.metacritic.com/search/all/" + name + "/results"
            browser.get(url)
            metaGameXpath = '//*[@id="main_content"]/div/div[3]/div/ul/li[1]/div/div[2]/div/span'
            metaGameElement = browser.find_element(By.XPATH, metaGameXpath)
            metaScoreText = metaGameElement.get_attribute("innerHTML")
            self.metaScoreList.append((str(metaScoreText)))
        except:
            self.metaScoreList.append(0)
        browser.close()

    def gameHowLongToBeat(self, name):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.implicitly_wait(2)
        try:
            url = "https://howlongtobeat.com/?q=" + name
            browser.get(url)
            timeGameXpath = '//*[@id="search-results-header"]/ul/li[1]/div[2]/div/div/div[2]'
            timeGameElement = browser.find_element(By.XPATH, timeGameXpath)
            timeGameText = timeGameElement.get_attribute("innerHTML")
            self.howLongList.append(str(timeGameText))
        except:
            self.howLongList.append("Not Found")
        browser.close()

    def gameImages(self, games):
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.implicitly_wait(2)
        for name in games:
            try:
                url = "https://howlongtobeat.com/?q=" + name
                browser.get(url)
                gameImageSelector = 'div.GameCard_search_list_image__iEl6K>a>img'
                gameImageElement = browser.find_element(By.CSS_SELECTOR, gameImageSelector)
                imageLink = gameImageElement.get_attribute("src")
                self.srcImagesList.append(imageLink)
            except:
                self.srcImagesList.append("Not Found")
        browser.close()


    def gameFactory(self, games):
        i = 0
        self.gameImages(games)
        for game in games:
            currTitle = game
            currPs = self.psPricesList[i]
            currAmazon = self.amazonPricesList[i]
            currmetaScore = self.metaScoreList[i]
            currhowLong = self.howLongList[i]
            currImageLinks = self.srcImagesList[i]
            try:
                self.database.insertGame(currTitle,(float)(currPs),(float)(currAmazon),(float)(currmetaScore),currhowLong,currImageLinks)
            except:
                print("NoGames")
            i += 1


fetcher = scrapper()
games = []

with open('games.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        games.append(row[0])
num_cores = mp.cpu_count()

star = time.time()

amazonPrices = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameAmazon)(i) for i in games)
metaScore = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameMetaCritic)(i) for i in games)
playStationPrices = Parallel(3, prefer = "threads")(delayed(fetcher.gamePlayStation)(i) for i in games)
metaScore = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameHowLongToBeat)(i) for i in games)
fetcher.gameFactory(games)
end = time.time()

print(end-star)




