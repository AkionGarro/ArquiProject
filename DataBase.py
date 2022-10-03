import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tcp:gardevserver.database.windows.net,1433;'
                      'Database=projectGarDev;Uid=gardev;'
                      'Pwd={Garroakion2908};Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')
cursor = cnxn.cursor()
cursor.execute("SELECT gamename from dbo.Games")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

