import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tcp:gardevserver.database.windows.net,1433;'
                      'Database=projectGarDev;Uid=gardev;'
                      'Pwd={Garroakion2908};Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')
cursor = cnxn.cursor()
#sql = "{call dbo.spINSERT_NewGame(1,'last of us',25,20,87,'35 horas','https://howlongtobeat.com/games/69695_Need_For_Speed_Heat.jpg?width=100');}"

cursor.execute("INSERT INTO Games (id,gameName,playPrice,amazonPrice,metaScore,howlong,imageLink) VALUES(5,'last of us',25,20,87,'35 horas','https://howlongtobeat.com/games/69695_Need_For_Speed_Heat.jpg?width=100');")
cursor.commit()