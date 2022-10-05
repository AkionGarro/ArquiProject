from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import multiprocessing as mp
from joblib import Parallel, delayed
import csv

# psPricesList = []
# amazonPricesList = []
# metaScoreList = []
# howLongList = []
# srcImagesList = []
# AllGamesList = []


class gameFull():
    def __init__(self, title, psPrice, amazonPrice, metaScore, howlong):
        self.title = title
        self.psPrice = psPrice
        self.amazonPrice = amazonPrice
        self.metaScore = metaScore
        self.howlong = howlong

    def printGameInfo(self):
        print("Name: " + self.title + "\n"
        "PlayStationPrice: " + self.psPrice + "\n"
        "AmazonPrice: " + self.amazonPrice + "\n"
        "Meta Score: " + self.metaScore + "\n"
        "How Long to Beat: " + self.howlong + "\n")

class scrapper:

    def __init__(self):
        self.psPricesList = []
        self.amazonPricesList = []
        self.metaScoreList = []
        self.howLongList = []
        self.srcImagesList = []
        self.AllGamesList = []

    def searchTopGames(self):

        games = []
        url = "https://www.3djuegos.com/top-100/ps4/"
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)
        browser.get(url)
        for i in range(1, 80):
            gameSelector = '#tb926 > div.izq2 > div.mar_t5.bgc0.br3.mar_rl3.s11.c7 > div.pad_rl8.fftext > table:nth-child(3) > tbody > tr:nth-child(' + str(
                i) + ') > td:nth-child(3) > a '
            gameElement = browser.find_element(By.CSS_SELECTOR, gameSelector)
            gameName = gameElement.get_attribute("innerHTML")
            games.append(gameName)
            #print(gameName)
        browser.close()
        return games

    def gamePlayStation(self, game):
        #global psPricesList
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)

        try:

            url = "https://store.playstation.com/es-cr/search/" + game
            browser.get(url)
            playGameXpath = '//*[@id="main"]/section/div/ul/li[1]/div/a/div/div'
            gameTitleElement = browser.find_element(By.XPATH, playGameXpath)
            gameTitleElement.click()
            gamePriceClass = 'psw-t-title-m'
            gamePriceElement = browser.find_element(By.CLASS_NAME, gamePriceClass)
            gamePriceText = gamePriceElement.get_attribute("innerHTML")
            self.psPricesList.append(str(gamePriceText))
        except:
            self.psPricesList.append("Not Found")

        browser.close()

    def gameAmazon(self, game):
        #global amazonPricesList
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)

        try:

            url = "https://www.amazon.com/s?k=" + game + " PlayStation 4 Game"
            browser.get(url)
            gameTitleElement = browser.find_element(By.CSS_SELECTOR, 'img.s-image')
            gameTitleElement.click()
            gamePriceID = 'priceblock_ourprice'
            gamePriceElement = browser.find_element(By.ID, gamePriceID)
            gamePriceText = gamePriceElement.get_attribute("innerHTML")
            self.amazonPricesList.append(str(gamePriceText))
            #print(gamePriceText)
        except:
            self.amazonPricesList.append("Not Found")
        browser.close()

    def gameMetaCritic(self, name):
        #global metaScoreList
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
            self.metaScoreList.append(str(metaScoreText))
            #print(metaScoreText)
        except:
            self.metaScoreList.append("Not Found")
        browser.close()

    def gameHowLongToBeat(self, name):
        #global howLongList
        service = Service(verbose=True)
        options = Options()
        options.add_argument("headless")
        browser = webdriver.Edge(service=service, options=options)

        try:

            url = "https://howlongtobeat.com/?q=" + name
            browser.get(url)
            timeGameXpath = '//*[@id="search-results-header"]/ul/li[1]/div[2]/div/div/div[2]'
            timeGameElement = browser.find_element(By.XPATH, timeGameXpath)
            timeGameText = timeGameElement.get_attribute("innerHTML");
            self.howLongList.append(str(timeGameText))
            #print(timeGameText)
        except:
            self.howLongList.append("Not Found")
        browser.close()

    def gameFactory(self, games):
        #
        i = 0
        for game in games:
            currTitle = game
            currPs = self.psPricesList[i]
            currAmazon = self.amazonPricesList[i]
            currmetaScore = self.metaScoreList[i]
            currhowLong = self.howLongList[i]
            currentGame = gameFull(currTitle, currPs, currAmazon, currmetaScore, currhowLong)
            self.AllGamesList.append(currentGame)
            i += 1
        return self.AllGamesList

    def printsGlobals(self):
        print('Lista ps: ' + str(self.psPricesList) + '\n'
        'Lista amazon: ' + str(self.amazonPricesList) + '\n'
        'Lista howlong: ' + str(self.howLongList) + '\n'
        'lista metas: ' + str(self.metaScoreList) + '\n')


fetcher = scrapper()
games = []
with open('games2.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        games.append(row[0])
num_cores = mp.cpu_count()


playStationPrices = Parallel(4, prefer = "threads")(delayed(fetcher.gamePlayStation)(i) for i in games)
amazonPrices = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameAmazon)(i) for i in games)
metaScore = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameMetaCritic)(i) for i in games)
metaScore = Parallel(mp.cpu_count(), prefer = "threads")(delayed(fetcher.gameHowLongToBeat)(i) for i in games)

fetcher.gameFactory(games)

print('Variables globales:')
fetcher.printsGlobals()
for i in fetcher.AllGamesList:
    i.printGameInfo()