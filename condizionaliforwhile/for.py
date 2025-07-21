# CICLO FOR IN PYTHON

# 1): Creare una variabile parola con valori casuali. Mandare a schermo ciascuna lettera della parola

parola = "alberto"

for lettera in parola:
    print(lettera)

# 2): Creare una variabile lista con valori casuali. Mandare a schermo con un ciclo for

lista_frutta = ["fragola", "melone", "limone", "anguria"]

for parola in lista_frutta:
    print(parola)

# 3): Mandare a schermo solo i numeri pari nel range () compreso tra 5 e 100 (non compreso)

for valore in range(5, 100):
    if valore % 2 == 0:
        print(valore)

# 4): Stampare con print() tutti i nomi delle celle di una scacchiera, sapendo che le righe 
# sono numerate e le colonne nominate con lettere

righe = range(1,9)
colonne = "abcdefgh"

for colonna in colonne:
    for riga in righe:
        print(colonna + ":" + str(riga))

# 5): Creare una lista inserendo un numero a piacere di parole. Mandare a schermo tutte 
# le parole con lunghezza pari ed in aggiunta le singole vocali che le compongono

parole = ["stizzoli", "luca", "alberto", "carlo", "anna"]

for parola in parole:
    if len(parola) % 2 == 0:
        print(parola)
        for vocale in parola:
            if vocale in "aeiou":
               print(vocale)

# 6): Creare 2 liste di numeri separati, iterare la prima lista e mandare a schermo 
# il numero solo se parte anche della seconda

lista_uno = [1, 2, 3, 4, 5]
lista_due = [10, 5, 6, 7, 2]

for valore in lista_uno:
    if valore in lista_due:
        print(valore)

# 7): Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista

lista = ["penna", "matita", "gomma", "righello"]

for elemento in lista:
    print(elemento)
    
# 8): Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.

for numero in range(1, 11):
    print(numero)

# 9): Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.

lista = [2, 5, 8, 10]
somma = 0

for numero in lista:
    somma += numero

print("La somma è:", somma)

# 10): Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.

for numero in range(2, 21, 2):
    print(numero)

# 11): Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.

stringa = "ciao a tutti"

for lettera in stringa:
    print(lettera)

# 12): Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario

dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}

for chiave in dizionario:
    print(chiave)

# 13): Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.

dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}

for chiave, valore in dizionario.items():
    print(chiave, ":", valore)

# 14):  Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista

lista = ["ciao", "a", "tutti"]

for parola in lista:
    for lettera in parola:
        print(lettera)

# 15):  Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.

stringa = "banana"
conta_a = 0

for lettera in stringa:
    if lettera == "a":
        conta_a += 1

print("La lettera a compare", conta_a, "volte.")

# 16):  Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.

lista = [4, 6, 8, 10, 2]
somma = 0

for numero in lista:
    somma += numero

media = somma / len(lista)
print("La media è:", media)

