import pyodbc
from flask import Flask
import json
class AzureConnection():
    def __init__(self):
        self.database = pyodbc.connect('Driver={SQL Server};'
                      'Server=tcp:gardevserver.database.windows.net,1433;'
                      'Database=projectGarDev;Uid=gardev;'
                      'Pwd={Garroakion2908};Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')
        self. cursor = self.database.cursor()

    def insertData(self,idGame,name,play,amazon,score,timeGame,image):
        self.cursor.execute("INSERT INTO Games (id,gameName,playPrice,amazonPrice,metaScore,howlong,imageLink) VALUES(?,?,?,?,?,?,?)",(idGame,name,play,amazon,score,timeGame,image))
        self.cursor.commit()


    def insertGame(self,idGame,name,play,amazon,score,timeGame,image):
        sql = "EXEC spINSERT_NewGame @id=?,@name=?,@playPrice=?,@amazonPrice=?,@meta=?,@howlong=?,@image=?"
        self.cursor.execute(sql,(idGame,name,play,amazon,score,timeGame,image))
        self.cursor.commit()

    def getGames(self):
        data = []
        sql = "SELECT * from dbo.Games"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            game ={"Id: ":row[0],"Name: ":row[1],"PlayStation Price:":row[2],"Amazon Price: ":row[3],"Meta Score:":row[4],"How Long to Beat: ":row[5] ,"Image: ": row[6]}
            data.append(game)
        return data





#conn = AzureConnection()
#conn.callProcedure(8,'last of us',25,20,87,'35 horas','https://howlongtobeat.com/games/69695_Need_For_Speed_Heat.jpg?width=100')
#games = conn.getGames()
#print("hello")
#sql = "{call dbo.spINSERT_NewGame(1,'last of us',25,20,87,'35 horas','https://howlongtobeat.com/games/69695_Need_For_Speed_Heat.jpg?width=100');}"

#cursor.execute("INSERT INTO Games (id,gameName,playPrice,amazonPrice,metaScore,howlong,imageLink) VALUES(5,'last of us',25,20,87,'35 horas','https://howlongtobeat.com/games/69695_Need_For_Speed_Heat.jpg?width=100');")
#cursor.commit()


