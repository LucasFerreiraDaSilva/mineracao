#!/usr/bin/python3

import csv

table = []; column = 2; summ = 0; count = 0; avgL = []; rCountry = []

with open('tabela.csv', 'r') as csvfile:
	for line in csvfile:
		table.append(line[:-1].split('","'))

for column in range(2,14):
	nullPoints = []
	for i in range(2, len(table)):
		table[i][13] = table[i][13].replace('"', "")
		lNum = table[i][column].replace('"', "").split(" ")
		if len(lNum) > 1:
			aux = 0
			for j in range(len(lNum)):
				aux = aux + float(lNum[j])
			avg = aux / (len(lNum))
			summ = summ + avg
			count = count + int(len(lNum))
		elif lNum[0] != '':
			summ = summ + float(lNum[0])
			count = count + 1
		elif lNum[0] == '':
			nullPoints.append([i, column])
	avg = summ/count; avgL.append(round(avg, 1))
	for i in range(len(nullPoints)):
		table[nullPoints[i][0]][nullPoints[i][1]] = round(avg, 1)

for i in range(2, 854):
	table[i][0] = table[i][0].replace('"', "")
	table[i][1] = table[i][1].replace(" ", "")
	lPais = table[i][1].split("-")
	if len(lPais) > 1:
		rCountry.append([table[i][0], 1 + (int(lPais[1]) - int(lPais[0])), lPais[0], i])

count = 0
for i in range(len(rCountry)):
	del table[rCountry[i][3]]
	count = count + 1
	if i != len(rCountry) - 1:
		rCountry[i + 1][3] = rCountry[i + 1][3] - count

for i in range(len(rCountry)):
	for j in range(rCountry[i][1]):
		table.append([rCountry[i][0], int(rCountry[i][2]) + j,avgL[0], avgL[1], avgL[2], avgL[3], avgL[4], avgL[5], avgL[6], avgL[7], avgL[8], avgL[9], avgL[10], avgL[11]])

table.sort(key=lambda x : x[0])

with open('new_csv.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",", escapechar=";")
    for i in range(len(table)):
    	if i == 0:
    		spamwriter.writerow([""] + [""] + table[i][2:14])
    	elif i == 1:
    		spamwriter.writerow(["Country"] + table[i][1:14])
    	else:
    		spamwriter.writerow(table[i])