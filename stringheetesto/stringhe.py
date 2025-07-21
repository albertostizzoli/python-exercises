# METODI DELLE STRINGHE IN PYTHON

# 1): Assegnare una stringa "ciao mondo" ad una variabile "stringa" 
# e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.

stringa = "ciao alberto"

stringa_maiuscola = stringa.upper()

print(stringa_maiuscola)

# 2): Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" 
# e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile.

stringa = "BENVENUTI A ROMA"

stringa_minuscola = stringa.lower()

print(stringa_minuscola)

# 3): Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" 
# e utilizzare il metodo split() per dividere la stringa in una lista di parole.

stringa = "Il meglio deve ancora venire"

stringa_divisa = stringa.split()

print(stringa_divisa)

# 4): Assegnare una stringa "Hello World" ad una variabile "stringa" 
# e utilizzare il metodo replace() per sostituire "World" con "Python".

stringa = "Hello World"

parola_nuova = stringa.replace("World", "Python")

print(parola_nuova)

# 5): Assegnare una stringa " Ciao " ad una variabile "stringa" 
# e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..

stringa = "   Ciao   "

parola_nuova = stringa.strip()

print(parola_nuova)

# 6): Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.

stringa = "abcdefg"

tre_caratteri = stringa[:3]

print(tre_caratteri)

# 7): Assegnare una stringa "Python" ad una variabile "stringa" 
# e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".

stringa = "Python"

starts_with_py = stringa.startswith("Py")

print(starts_with_py)

# 8): Assegnare una stringa "Ciao mondo" ad una variabile "stringa" 
# e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.

stringa = "Ciao mondo"

conteggio = stringa.count("o")

print(conteggio)

# 9): Assegnare una stringa "Ciao mondo" ad una variabile "stringa". 
# Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

stringa = "Ciao mondo"

nuova_stringa = stringa[-5:].upper().replace("O", "K")

print(nuova_stringa)