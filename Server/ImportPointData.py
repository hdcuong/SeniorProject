import csv, sqlite3

con = sqlite3.connect("laptop.db")
cur = con.cursor()
with open('PointRank.csv') as data:
    next(data)
    readcsv = csv.reader(data, delimiter=',')
    for row in readcsv:
        to_db = [row[0], row[1], row[2], row[3], row[4], row[5]]
        cur.execute("INSERT INTO POINTLAPTOP (ID, GAME, BUSINESS, STUDENT, DESIGN, VGA) VALUES (?, ?, ?, ?, ?, ?);", to_db)
        con.commit()
con.close()

