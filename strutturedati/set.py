# I SET IN PYTHON

# 1): Creare un set vuoto e assegnarlo a una variabile.

mio_set = set()
print(mio_set)

# 2): Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".

set_frutta = {"mela", "banana", "kiwi", "mela"}
print(set_frutta)

# 3): Aggiungere l'elemento "pesca" al set precedente.

set_frutta = {"mela", "banana", "kiwi", "mela"}
set_frutta.add("pesca")
print(set_frutta)

# 4): Rimuovere l'elemento "mela" dal set precedente.

set_frutta = {"mela", "banana", "kiwi", "mela"}
set_frutta.remove("mela")
print(set_frutta)

# 5): Verificare se l'elemento "ananas" è presente nel set precedente.

set_frutta = {"mela", "banana", "kiwi", "mela"}
if "ananas" in set_frutta:
    print("L'ananas c'è nel set")
else: 
    print("L'ananas non c'è nel set")

# 6): Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".

nuovo_set = {"banana", "kiwi", "arancia"}

print(nuovo_set)

# 7): Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().

numeri = set(range(1, 6))

print(numeri)

# 8): Creare un nuovo set contenente i numeri pari del set precedente.

numeri = set(range(1, 6))

print(numeri)
numeri_pari = set(x for x in numeri if x % 2 == 0)

print(numeri_pari)

# 9): Creare un set e una lista di numeri interi. 
# Stampare solo i numeri che sono presenti sia nel set che sulla lista

set_numeri = {2, 4, 6, 8, 10}
lista_numeri = [4, 8, 12, 16, 20]

for numero in set_numeri:
    if numero in lista_numeri:
        print(numero)

# 10): Creare un set di tuple in cui ogni tupla contiene due numeri interi. 
# Stampare le tuple in cui la somma dei due numeri è pari

set_di_tuple = {(1, 2), (3, 4), (5, 6), (6, 8)}

for tupla in set_di_tuple:
    if (tupla[0] + tupla[1]) % 2 == 0:
        print(tupla)

