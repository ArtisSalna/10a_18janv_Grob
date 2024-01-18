import csv

def lasit_izdrukat(csv_fails):
    with open(csv_fails, 'r', newline='', encoding="utf-8")as ff:
        csvlasitajs=csv.reader(ff)
        for rinda in csvlasitajs:
            if len(rinda) > 1:
                print(rinda[1])
lasit_izdrukat('2uzd.csv')
