# LE FUNZIONI IN PYTHON

# 1): Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.

lista_numeri = [1, 2, 3, 4, 5, 6]

def somma_lista(lista_numeri):
    somma = 0
    for numero in lista_numeri:
        somma += numero
    return somma

print(somma_lista(lista_numeri))

# 2): Scrivi una funzione che prende una stringa e restituisce la stringa invertita

def stringa_invertita(stringa):
    parola_invertita = stringa[::-1]
    return parola_invertita
    
stringa = "Radar"
palindromo = stringa_invertita(stringa)
    

print(palindromo)

# 3): Scrivi una funzione che prende una lista di parole e restituisce una lista contenente 
# solo le parole che iniziano con una lettera specificata

lista_parole = ["spesa", "casa", "disegno", "dormire"]

def parole_con_lettera(lista_parole, lettera):
    risultato = []
    for parola in lista_parole:
        if parola[0] == lettera:
            risultato.append(parola)
    return risultato

lettera = "s"
    
print(parole_con_lettera(lista_parole, lettera))

# 4): Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari

lista_numeri = [1, 2, 3, 4, 5, 6]

def numeri_pari(lista_numeri):
    risultato = []
    for numero in lista_numeri:
        if numero % 2 == 0:
            risultato.append(numero)
    return risultato
        
print(numeri_pari(lista_numeri))

# 5): Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.

lista_parole = ["spesa", "casa", "disegno", "dormire"]

def lunghezza_parole(lista_parole):
    risultato = []
    for parola in lista_parole:
        risultato.append(len(parola))
    return risultato
    
print(lunghezza_parole(lista_parole))

# 6): Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo

lista_numeri = [1, 2, 3, 4, 5, 6]

def valore_massimo(lista_numeri):
    massimo = lista_numeri[0]
    for numero in lista_numeri:
        if numero > massimo:
            massimo = numero
    return massimo
        
print(valore_massimo(lista_numeri))

# 7): Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga

lista_parole = ["spesa", "casa", "disegno", "dormire", "dinosauro"]

def parola_lunga(lista_parole):
    piu_lunga = lista_parole[0]
    for parola in lista_parole:
        if len(parola) > len(piu_lunga):
            piu_lunga = parola
    return piu_lunga
        
print(parola_lunga(lista_parole))

# 8): Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri

lista_numeri = [1, 2, 3, 4, 5, 6]

def media_numeri(lista_numeri):
    somma = 0
    for numero in lista_numeri:
        somma += numero
        media = somma / len(lista_numeri)
    return media
    
print(media_numeri(lista_numeri))

# 9): Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome

lista = ["ciao", "alberto", "anna", "radar"]

def parole_palindrome(lista):
    risultato = []
    for parola in lista:
        if parola == parola[::-1]:
            risultato.append(parola)
    return risultato

print(parole_palindrome(lista))

# 10): Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.

lista = [1, 2, 3, 4, 5, 6]

def numeri_maggiori_di(lista, valore):
    risultato = []
    for numero in lista:
        if numero > valore:
            risultato.append(numero)
    return risultato

valore = 2

print(numeri_maggiori_di(lista, valore))

