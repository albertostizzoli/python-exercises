#  FORMATTAZIONE DELLE STRINGHE IN PYTHON

# 1): Creare due variabili "nome" e "cognome" e concatenarle a schermo.

nome = "Alberto"
cognome = "Stizzoli"

print(nome + " " + cognome)

# 2): Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".

numero = 42
stringa = "Il numero è {}".format(numero)
print(stringa)

# 3): Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". 
# Per il binario utilizzare bin(numero)

numero = 42
stringa = "Il numero binario di {} è {}".format(numero, bin(numero))
print(stringa)

# 4): Partendo dalla variabile "numero" uguale a 5, 
# utilizzare le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".

numero = 5
stringa = f"Il quadrato di {numero} è {numero ** 2}"

print(stringa)

# 5): Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere 
# "Il mio nome è {nome} ed il cognome è {cognome}". Come da esempio dovete fare riferimento al nome delle variabili 
# e non alla posizione usata dentro format.

nome = "Alberto"
cognome = "Stizzoli"
stringa = "Il mio nome è {nome} e cognome è {cognome}".format(nome = nome, cognome = cognome)
print(stringa)

# 6): Facendo riferimento all'esercizio precedente ottenere il seguente risultato modificando i valori nel format(): 
# "Il mio nome è LUCA ed il cognome è RoKKi”

nome = "Alberto"
cognome = "Stizzoli"
stringa = "Il mio nome è {nome} e cognome è {cognome}".format(nome = nome.upper(), cognome = cognome.replace("Stizzoli", "RoKKI"))
print(stringa)