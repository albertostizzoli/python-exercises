# CICLO WHILE IN PYTHON

# 1): Stampare i numeri interi da 1 a 10 usando un loop while.

x = 1

while x <= 10:
    print(x)
    x += 1

# 2): Calcolare la somma dei primi n numeri interi positivi usando un loop while. 
# L'utente deve inserire il valore di numbers

numbers = int(input("Inserisci i numeri primi da sommare: "))
sum = 0
i = 1
while i <= numbers:
    sum += i
    i += 1
print("La somma dei primi", numbers, "numeri interi positivi è", sum)


# 3): Stampare i numeri pari da 2 a 10 usando un loop while.

i = 2
while i <= 10:
    print(i)
    i += 2

# 4): Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. 
# Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. 
# Usare un loop while.

import random

num = random.randint(1, 10)
guess = int(input("Indovina un numero compreso tra 1 e 10: "))

while guess != num:
    guess = int(input("Sbagliato. Prova ancora: "))

print("Indovinato!")

# 5): Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.

s = input("Inserisci una stringa: ")
i = len(s) - 1

while i >= 0:
    print(s[i], end="")
    i -= 1

# 6): Stampare i numeri da 10 a 1 usando un loop while.

i = 10
while i >= 1:
    print(i)
    i -= 1

# 7): Calcolare il fattoriale di un numero intero positivo n usando un loop while.

n = int(input("Inserisci un valore per n: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Il fattoriale di", n, "è", fact)

# 8): Chiedere all'utente di inserire una lista di numeri interi. 
# Stampare la somma di tutti i numeri usando un loop while.

lst = []
n = int(input("Quanti numeri vuoi inserire? "))
i = 0
while i < n:
    num = int(input("Inserisci un numero: "))
    lst.append(num)
    i += 1
sum = 0
i = 0
while i < len(lst):
    sum += lst[i]
    i += 1
print("La somma di tutti i numeri è", sum)

# 9): Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.

s = input("Inserisci una stringa: ")
i = 0

while i < len(s):
    if s[i] not in "aeiouAEIOU":
        print(s[i], end="")
    i += 1


