#!/usr/bin/env python3

n = 0
tabela = []
tb_aux = []
tb_aux2 = []

arquivo = open('tabela.csv', 'r+')

# trasforma o arquivo em uma lista de listas
for linha in arquivo:
    listl = linha.split('",')
    ll = []
    for i in listl:
        ll.append(i.replace('"',''))
    tb_aux.append(ll)

# remove os "\n" do final das linhas
for linha in tb_aux:
    ll = []

    for i in linha:
        ll.append(i.replace('\n',''))
    tb_aux2.append(ll)

# busca as colunas que possuem mais de um valor e faz a media entre eles, substituindo-os
for l in tb_aux2[2:]:
    ll = []
    ll.append(l[0])
    ll.append(l[1])

    for i in range(12):
        v = l[i+2].split(" ")

        if len(v) > 1:
            s = 0.0
            for val in v:
                s += float(val)
            dado = "%.2f" % (s/len(v))

        elif len(v) == 1 and v[0] != '':
            dado = "%.2f" % float(v[0])

        else:
            dado = ''

        ll.append(dado)
    tabela.append(ll)

paises = []
p1 = tabela[2:][0][0]
paises.append(p1)

# cria uma lista de paises distintos para usar na media de cada grupo depois
for linha in tabela[2:]:
    p2 = linha[0]
    if p1 != p2:
        p1 = p2
        paises.append(p1)

    else:
        continue

tb_paises = []
soma = []

# zera a lista das somas, que sera usada para caucular a media por pais
for i in range(12):
    soma.append(0.0)

'''
# inacabado...
for g in paises:
    for l in tabela[2:]:
        if g == l[0]

for x in tabela[2:]:
    print (x)

'''
for x in paises:
    print (x)
'''
