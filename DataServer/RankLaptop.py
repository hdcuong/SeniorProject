import csv

f = csv.writer(open('PointRank.csv', 'w'))
f.writerow(['ID', 'GAME', 'BUSINESS', 'STUDENT', 'DESIGN', 'VGA'])

#Calculator point of Game
def gamePoint(screen, cpu, ram):
    return (screen*0.3 + cpu*0.35 + ram*0.35)

#Calculator point of Business
def businessPoint(screen, cpu, ram):
    return (screen*0.2 + cpu*0.4 + ram*0.4)

#Calculator point of Student
def studentPoint(screen, cpu, ram):
    return (screen*0.5 + cpu*0.25 +ram*0.25)

#Calculator point of Design
def designPoint(screen, cpu, ram):
    return (screen*0.4 + cpu*0.3 + ram*0.3)

#Write rank point of fpt to file

with open('laptoppointfpt.csv') as miningfile:
    next(miningfile)
    readcsv = csv.reader(miningfile, delimiter = ',')
    for row in readcsv:
        a = int(row[1])
        b = int(row[2])
        c = int(row[3])
        d = int(row[4])
        ID = row[0]
        game = format(gamePoint(a, b, c), '.2f')
        business = format(businessPoint(a, b, c), '.2f')
        student = format(studentPoint(a, b, c), '.2f')
        design = format(designPoint(a, b, c), '.2f')
        vga = d
        f.writerow([ID, game, business, student, design, vga])
#Write rank point of tgdd to file

with open('laptoppointtgdd.csv') as miningfile:
    next(miningfile)
    readcsv = csv.reader(miningfile, delimiter = ',')
    for row in readcsv:
        a = int(row[1])
        b = int(row[2])
        c = int(row[3])
        d = int(row[4])
        ID = row[0]
        game = format(gamePoint(a, b, c), '.2f')
        business = format(businessPoint(a, b, c), '.2f')
        student = format(studentPoint(a, b, c), '.2f')
        design = format(designPoint(a, b, c), '.2f')
        vga = d
        f.writerow([ID, game, business, student, design, vga])