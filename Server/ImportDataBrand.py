import csv, sqlite3

con = sqlite3.connect("laptop.db")
cur = con.cursor()

#Brand for fpt

with open('miningdatafpt.csv') as data:
    next(data)
    readcsv = csv.reader(data, delimiter=',')
    a = 0
    for row in readcsv:
        a = a + 1
        id = str(a) + 'FPT'
        to_db = [id, row[0], row[1]]
        cur.execute("INSERT INTO BRANDFPT (ID, BRAND, PRICE) VALUES (?, ?, ?);", to_db)
        con.commit()

#Brand for tgdd

with open('miningdatatg.csv') as data:
    next(data)
    readcsv = csv.reader(data, delimiter=',')
    a = 0
    for row in readcsv:
        a = a + 1
        id = str(a) + 'TGDD'
        to_db = [id, row[0], row[1]]
        cur.execute("INSERT INTO BRANDTGDD (ID, BRAND, PRICE) VALUES (?, ?, ?);", to_db)
        con.commit()

con.close()

