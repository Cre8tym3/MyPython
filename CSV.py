import csv
exampleFile = open('acctclasskey.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    spo = str(row)
    spop = spo.split(';')
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row) + spop[0])
