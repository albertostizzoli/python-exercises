# CONDIZONALI IF/ELIF/ELSE IN PYTHON

# 1): Scrivere un programma che chiede all'utente di inserire un numero e stampa 
# "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo”

numero = int(input("Inserisci un numero: "))

if numero > 0:
    print("Il numero è positivo")
else:
    print("Il numero è negativo")

# 2): Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore"
#  se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo,
#  altrimenti stampa "I numeri sono uguali"

numero1 = int(input("Inserisci il primo numero"))
numero2 = int(input("Inserisci il secondo numero"))

if numero1 > numero2:
    print("il primo numero è maggiore del secondo")
elif numero2 > numero1:
    print("il secondo numero è maggiore del primo")
else:
    print("I numeri sono uguali")

# 3): Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, 
# altrimenti stampa "La stringa non è vuota".

stringa = input("Inserisci una stringa: ")

if not stringa:
    print("la stringa è vuota")
else:
    print("la stringa non è vuota")

# 4): Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" 
# se il numero è pari, altrimenti stampa "Il numero è dispari".

numero = int(input("Inserisci un numero: "))
if numero % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")

# 5): Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" 
# se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".

lettera = input("Inserisci una lettera: ")

if lettera in "aeiou":
    print("la lettera è una vocale")
else:
    print("la lettera non è una vocale")

# 6): Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" 
# se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".

numero = int(input("Inserisci un numero: "))

if 1 <= numero <= 10:
    print("il numero è compreso tra 1 e 10")
else:
    print("il numero non è compreso tra 1 e 10")

# 7): Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, 
# stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". 
# Se il numero è minore di 10, stampare "Il numero è minore di 10".

numero = int(input("Inserisci un numero: "))

if numero > 10:
    print("il numero è maggiore di 10")
elif numero == 10:
    print("il numero è uguale a 10")
else:
    print("il numero è minore di 10")

# 8): Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u) 
# con isalpha(), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante, 
# stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare 
# "Il carattere inserito non è una lettera".

carattere = input("Inserisci un carattere: ")

if carattere in "aeiou":
    print("Il carattere inserito è una vocale")
elif carattere.isalpha():
    print("Il carattere inserito è una consonante")
else:
    print("Il carattere inserito non è una lettera")

# 9): Scrivi un programma che chieda all'utente di inserire tre numeri interi che rappresentano i lati di un triangolo. 
# Il programma deve verificare se questi tre numeri formano un triangolo rettangolo. 
# Se i tre numeri soddisfano la condizione per essere un triangolo rettangolo (cioè rispettano il teorema di Pitagora), 
# allora stampa "I tre numeri formano un triangolo rettangolo". Altrimenti, stampa "I tre numeri non formano un triangolo rettangolo".

a = int(input("Inserisci il primo lato: "))
b = int(input("Inserisci il secondo lato: "))
c = int(input("Inserisci il terzo lato: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("I tre numeri formano un triangolo rettangolo")
else:
    print("I tre numeri non formano un triangolo rettangolo")