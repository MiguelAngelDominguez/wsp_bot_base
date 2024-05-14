import csv

PATH_FILE = './database/date_yachay.csv'

with open(PATH_FILE, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))