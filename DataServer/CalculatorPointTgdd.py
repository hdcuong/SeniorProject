import csv

f = csv.writer(open('laptoppointtgdd.csv', 'w'))
f.writerow(['ID', 'Screen', 'CPU', 'RAM', 'VGA'])

#Write functions for calculator point

#Calculator point of Screen
def CalPointScreen(screen):
    if float(screen) < 14:
        return 5
    elif float(screen) >= 15:
        return 9
    else:

        return 7

#Calculator point of RAM
def CalPointRam(ram):
    if int(ram) < 4:
        return 5
    elif int(ram) >= 8:
        return 9
    else:
        return 7

#Calculator point of CPU
def CalPointCpu(cpu):
    verylow = ['Celeron', 'Pentium']
    low = ['R3', 'i3', 'M3']
    medium = ['R5', 'i5', 'I5']
    high = ['i7', 'R7']
    veryhigh = ['1950x', 'i9']
    if any(ext in cpu for ext in verylow):
        return 4
    elif any(ext in cpu for ext in low):
        return 5
    elif any(ext in cpu for ext in medium):
        return 7
    elif any(ext in cpu for ext in high):
        return 9
    elif any(ext in cpu for ext in veryhigh):
        return 10

#Calculator point of VGA
def CalPointVga(vga):
    havevga = ['NVIDIA', 'AMD', 'GeForce', 'GTX', 'Radeon']
    if any(ext in vga for ext in havevga):
        return 1
    else:
        return 0

with open('miningdatatg.csv') as miningfile:
    next(miningfile)
    readcsv = csv.reader(miningfile, delimiter = ',')
    a = 0
    for row in readcsv:
        a = a + 1
        ID = str(a) + 'TGDD'
        screen = CalPointScreen(row[3])
        cpu = CalPointCpu(row[4])
        ram = CalPointRam(row[5])
        vga = CalPointVga(row[6])
        f.writerow([ID, screen, cpu, ram, vga])


    