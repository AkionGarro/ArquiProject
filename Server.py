from flask import Flask, jsonify, request

import DataBase

app = Flask(__name__)


@app.route('/games')
def getGamesDataBase():
    database = DataBase.AzureConnection()
    data = database.getGames()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
