cpu = 'Pentium ah ahi ahi ahi ahi'
verylow = ['Celeron', 'Pentium']
if any(ext in verylow for ext in cpu):
    print(4)
else:
    print(5)