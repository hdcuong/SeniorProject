import csv

number = "0123456789"
f = csv.writer(open('miningdatafpt.csv', 'w'))
f.writerow(['Brand', 'Price', 'Image', 'Screen', 'CPU', 'RAM', 'VGA', 'OS', 'Weight', 'Link'])

with open('datafpt.csv') as miningfile:
    next(miningfile)
    readcsv = csv.reader(miningfile, delimiter=',')
    for row in readcsv:
        #Mining Brand
        brand = row[0].split(" ")[0]
        #Mining Price
        price = ""
        s = row[1]
        for x in range(len(s)):
            for y in range(len(number)):
                if number[y] == s[x]:
                    price = price + number[y]
        #Mining Image
        image = row[2]
        #Mining Screen
        screen = float(row[3].split(" ")[0])
        #Mining CPU
        cpu = row[4]
        #Mining RAM
        ram = int((row[5]).split(" ")[0].rstrip('GB'))
        #Mining VGA
        vga = row[6]
        #Mining OS
        os = row[7]
        #Mining Weight
        weight = float((row[8].split(" "))[0].rstrip("kg"))
        #Mining Link
        link = row[9]
        #Save data to new csv file
        f.writerow([brand, price, image, screen , cpu, ram, vga, os, weight, link]) 
        