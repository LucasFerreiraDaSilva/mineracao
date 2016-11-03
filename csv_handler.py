#!/usr/bin/python3
import csv

table = []; column = 2; summ = 0; count = 0; Country = []; rCountry = []; country_region = []

def read_csv(table, name_table):
	with open(name_table, 'r') as csvfile:
		for line in csvfile:
			if name_table == "tabela.csv":
				table.append(line[:-1].split('","'))
			else:
				table.append(line[:-1].split(','))

def write_csv(table):
	with open('new_csv.csv', 'w', newline='') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=",", escapechar=";")
	    for i in range(1, len(table)):
	    	if i == 1:
	    		spamwriter.writerow(["Country"] + ["continent"] + ["regionUN"] + ["subregionUN"] + ["Year"] + ["Both Sexes"] + ["Female"] + ["Male"])
	    	elif len(table[i]) == 17 and (int(table[i][1]))>1999:
	    		spamwriter.writerow([table[i][0]] + [table[i][14]] + [table[i][15]] + [table[i][16]] + [table[i][1]] +  [table[i][5]] + [table[i][6]] + [table[i][7]])

def format_table(table):
	for i in range(2,len(table)):
		table[i][0] = table[i][0].replace('"', "")
		table[i][1] = table[i][1].replace(" ", "")
		table[i][13] = table[i][13].replace('"', "")

def insert_number(n, table, nullPoints):
	for i in range(len(nullPoints)):
		table[nullPoints[i][0]][nullPoints[i][1]] = round(n, 1)

def search_id(string):
	for i in range(len(Country)):
		if Country[i][0] == string:
			return i

def trade_specChar(table):
	for i in range(2, 14):
		table[0][i] = table[0][i].replace("&lt;", "< ")

read_csv(table, "tabela.csv")
read_csv(country_region, "paises.csv")
format_table(table)

# Laço responsável por definir os intervalos de cada país
i = 2
while i < len(table):
	atual_string = table[i][0];
	aux = 1
	id_ini = i
	while True:
		if i + aux > 853:
			break
		elif atual_string == table[i + aux][0]:
			aux = aux + 1
		else:
			break
	Country.append([atual_string, id_ini, aux - 1])
	i = i + aux

# Laço resposável por criar lista de países e suas respectivas médias por coluna
for i in range(0, len(Country)):
	id_base = Country[i][1]; id_lmit = Country[i][2]
	del Country[i][1]; del Country[i][1]
	for column in range(2, 14):
		nullPoints = []
		summ = 0; count = 0; j = 0
		while j <= id_lmit:
			lNum = table[id_base + j][column].split(" ")
			if len(lNum) > 1:
				aux = 0
				for z in range(len(lNum)):
					aux = aux + float(lNum[z])
				avg = aux / len(lNum)
				table[id_base + j][column] = float(round(avg, 1))
				summ = summ + avg
				count = count + len(lNum)
			if lNum[0] != '':
				summ = summ + float(lNum[0])
				count = count + 1
			elif lNum[0] == '':
				nullPoints.append([id_base + j, column])
			j = j + 1
		if count == 0:
			Country[i].append(0.0)
			insert_number(float(0.0), table, nullPoints)
			#continue
		else:
			avg = summ / count
			Country[i].append(round(avg, 1))
			insert_number(avg, table, nullPoints)


# Cria lista responsável pelos intervalos intra-país
for i in range(2, 854):
	lPais = table[i][1].split("-")
	if len(lPais) > 1:
		id_country = search_id(table[i][0])
		rCountry.append([table[i][0], 1 + (int(lPais[1]) - int(lPais[0])), lPais[0], i, id_country])

# Remove da lista principal as tuplas com anos intervalados.
count = 0
for i in range(len(rCountry)):
	del table[rCountry[i][3]]
	count = count + 1
	if i != len(rCountry) - 1:
		rCountry[i + 1][3] = rCountry[i + 1][3] - count

for i in range(len(rCountry)):
	for j in range(rCountry[i][1]):
		idC = rCountry[i][4]
		table.append([Country[idC][0], int(rCountry[i][2]) + j, Country[idC][1], Country[idC][2], Country[idC][3], Country[idC][4], Country[idC][6], Country[idC][6], Country[idC][7], Country[idC][8], Country[idC][9], Country[idC][10], Country[idC][11], Country[idC][12]])

# Busca região do pais e anexa os dados à tabela Country

for i in range(2, len(table)):
	for j in range(len(country_region)):
		if table[i][0] == country_region[j][0]:
			table[i].append(country_region[j][1])
			table[i].append(country_region[j][2])
			table[i].append(country_region[j][3])

table.sort(key=lambda x : x[0])
trade_specChar(table)
write_csv(table)
