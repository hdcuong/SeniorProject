import sqlite3 as sql
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlite3 import Error

con = sql.connect('laptop.db', check_same_thread=False)
cur = con.cursor()
app = Flask (__name__)

CORS(app)

@app.route ('/request/game',methods = ['GET'])
def game():
    if request.method == 'GET':
        try:
            price = request.values.get('price') 
            brand = request.values.get('brand')
            if brand == 'NoBrand':
                if price == '1':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.PRICE < 5000000 and PL.VGA = 1 ORDER BY PL.GAME DESC LIMIT 5")
                elif price == '2':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 5000000 <= BR.PRICE and BR.PRICE <= 10000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5")
                elif price == '3':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 10000000 <= BR.PRICE and BR.PRICE <= 15000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5")
                elif price == '4':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 15000000 <= BR.PRICE and BR.PRICE <= 20000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5")
                elif price == '5':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 20000000 <= BR.PRICE and BR.PRICE <= 25000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5")
                elif price == '6':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.PRICE > 25000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5")
            else:
                if price == '1':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND BR.PRICE < 5000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
                elif price == '2':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand +  "' AND 5000000 <= BR.PRICE and BR.PRICE <= 10000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
                elif price == '3':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 10000000 <= BR.PRICE and BR.PRICE <= 15000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
                elif price == '4':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 15000000 <= BR.PRICE and BR.PRICE <= 20000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
                elif price == '5':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 20000000 <= BR.PRICE and BR.PRICE <= 25000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
                elif price == '6':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND BR.PRICE > 25000000 and PL.VGA = 1 ORDER BY PL.GAME, IF.WEIGHT DESC LIMIT 5"
                    cur.execute(temp)
        except:
            con.rollback()
            columns = [column[0] for column in cur.description]
            results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)
con.close()