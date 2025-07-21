# LE LISTE COMPREHENSIONS IN PYTHON

# 1): Creare una list comprehension che genera i quadrati dei numeri da 1 a 10.

quadrati = [x**2 for x in range(1, 11)]
print(quadrati)

# 2): Utilizzare una list comprehension per convertire tutte le stringhe di una lista in maiuscolo.

parole = ["ciao", "mondo", "python"]
parole_maiuscole = [parola.upper() for parola in parole]
print(parole_maiuscole)

# 3): Scrivere una list comprehension che estrae solo i numeri pari da una lista.

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeri_pari = [x for x in numeri if x % 2 == 0]
print(numeri_pari)

# 4): Generare una lista delle lunghezze delle parole in una frase utilizzando list comprehensions.

frase = "List comprehensions in Python sono potenti"
lunghezze = [len(parola) for parola in frase.split()]
print(lunghezze)

# 5): Creare una list comprehension che include solo le stringhe di lunghezza superiore a 5 caratteri da una lista.

parole = ["casa", "albero", "sole", "programmazione", "python"]
parole_lunghe = [parola for parola in parole if len(parola) > 5]
print(parole_lunghe)

# 6): Utilizzare una list comprehension per creare una lista di tuple, ognuna contenente un numero e il suo quadrato.

numeri = range(1, 6)
tuples = [(x, x**2) for x in numeri]
print(tuples)

# 7): Scrivere una list comprehension che filtra i numeri dispari di una lista e calcola il cubo di ciascuno.

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubi_dispari = [x**3 for x in numeri if x % 2 != 0]
print(cubi_dispari)

# 8): Generare una lista di numeri interi casuali e utilizzare una list comprehension per selezionare solo quelli che sono multipli di 3

import random

numeri_casuali = [random.randint(1, 100) for _ in range(10)]
multipli_di_3 = [num for num in numeri_casuali if num % 3 == 0]
print(multipli_di_3)

# 9): Utilizzare una list comprehension per convertire una lista di gradi Fahrenheit in gradi Celsius.

fahrenheit = [32, 64, 100, 212]
celsius = [(f - 32) * 5/9 for f in fahrenheit]
print(celsius)

# 10): Creare una list comprehension che estrae le vocali da una stringa data.

stringa = "List comprehension in Python"
vocali = [char for char in stringa if char in 'aeiouAEIOU']
print(vocali)