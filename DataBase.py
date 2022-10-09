import pyodbc
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

    def insertGame(self,name,play,amazon,score,timeGame,image):
        sql = "EXEC spINSERT_NewGame2 @name=?,@playPrice=?,@amazonPrice=?,@meta=?,@howlong=?,@image=?"
        self.cursor.execute(sql,(name,play,amazon,score,timeGame,image))
        self.cursor.commit()

    def getGames(self):
        data = []
        sql = "SELECT * from dbo.Games"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            game ={"Id":row[0],"Name":row[1],"PlayStationPrice":str(row[2]),"AmazonPrice":str(row[3]),"Meta Score":str(row[4]),"HowLongtoBeat":row[5],"Image":row[6]}
            data.append(game)
        return data


#conn = AzureConnection()
#data = conn.getGames()
#print(data)


