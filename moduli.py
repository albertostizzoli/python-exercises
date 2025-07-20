# I MODULI IN PYTHON

# 1): Importa il modulo math e calcola la radice quadrata di 16

import math

print(int(math.sqrt(16)))

# 2): Importa il modulo random e genera un numero casuale compreso tra 1 e 10

import random

print(random.randint(1, 10))

# 3): Importa il modulo os e stampa la directory di lavoro corrente

import os

print(os.getcwd())

# 4): Importa il modulo datetime e stampa la data e l’ora corrente

import datetime

x = datetime.datetime.now()
print(x)

# 5): Importa il modulo csv e apri il file dati.csv 
# che contiene una tabella di dati separati da virgola. 
# Poi leggi il contenuto del file e stampalo.

import csv

with open('dati.csv', 'r') as file:
    lettore = csv.reader(file)
    for riga in lettore:
        print(riga)

# 6): Importa il modulo json e crea un dizionario con alcune chiavi e valori. 
# Poi serializza il dizionario in formato JSON e stampalo.

import json

dizionario = {'nome': 'Alberto', 'cognome': 'Stizzoli', 'eta': 31}
json_dizionario = json.dumps(dizionario)

print(json_dizionario)