from glob import glob
import pandas as pd
import csv

#CHANGE YOUR PATH
data_dirB = "E:\\Masaüstü\\BBC NEWS\\RAW\\bbc\\business"
data_dirE = "E:\\Masaüstü\\BBC NEWS\\RAW\\bbc\\entertainment"
data_dirP = "E:\\Masaüstü\\BBC NEWS\\RAW\\bbc\\politics"
data_dirS = "E:\\Masaüstü\\BBC NEWS\\RAW\\bbc\\sport"
data_dirT = "E:\\Masaüstü\\BBC NEWS\\RAW\\bbc\\tech"
#CHANGE YOUR PATH

filesB = glob(data_dirB + "/*.txt")
filesE = glob(data_dirE + "/*.txt")
filesP = glob(data_dirP + "/*.txt")
filesS = glob(data_dirS + "/*.txt")
filesT = glob(data_dirT + "/*.txt")
filesAll=[]
filesAll.append(filesB)
filesAll.append(filesT)
filesAll.append(filesS)
filesAll.append(filesP)
filesAll.append(filesE)
data = pd.DataFrame()
dic={}

for i in range(5):
    for j in range(len(filesAll[i])):

        label=-1
        if(filesB.__contains__(filesAll[i][j])):
            label=0
        elif (filesE.__contains__(filesAll[i][j])):
            label = 1
        elif (filesP.__contains__(filesAll[i][j])):
            label = 2
        elif (filesS.__contains__(filesAll[i][j])):
            label = 3
        elif (filesT.__contains__(filesAll[i][j])):
            label = 4
        string = open(filesAll[i][j], "r").read()
        string=string.replace("\n", " ")
        dic[string] = label


with open('BBC_NEWS_DATASET.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['string', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key in dic:
        writer.writerow({'string': key, 'label': dic[key]})


