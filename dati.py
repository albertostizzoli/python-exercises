# TIPI DI DATI IN PYTHON

# 1): Dichiarare una variabile "numero_intero" e assegnargli un valore intero. 
# Mandare a schermo il tipo della variabile per conferma.

numero_intero = 42
print(type(numero_intero))

#2):  Dichiarare una variabile "numero_decimale" e assegnargli un valore float. 
# Mandare a schermo il tipo della variabile per conferma.

numero_decimale = 3.14
print(type(numero_decimale))

# 3): Creare una variabile "testo" e assegnargli una stringa contenente una frase. 
# Mandare a schermo il tipo della variabile per conferma.

testo = "Ciao sono un testo"
print(type(testo))

# 4):  Creare una variabile "valore_booleano" e assegnargli un valore booleano. 
# Mandare a schermo il tipo della variabile per conferma.

valore_booleano = True
print (type(valore_booleano))

# 5): Creare una lista "numeri" contenente 5 numeri interi. 
# Mandare a schermo il tipo della variabile per conferma.

numeri = [1, 2, 3, 4, 5]
print (type(numeri))

# 6): Creare una lista "misti" contenente un numero intero, un numero float, 
# una stringa e un valore booleano. Mandare a schermo il tipo della variabile per conferma.

misti = [42, 3.14, "testo", True]
print(type(misti))

# 7): Creare una tupla "giorni_settimana" contenente i giorni della settimana come stringhe. 
# Mandare a schermo il tipo della variabile per conferma.

giorni = ("lunedi", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica")
print(type(giorni))

# 8): Creare un dizionario "informazioni_personali" contenente il tuo nome, cognome, età e città di residenza.
#  Mandare a schermo il tipo della variabile per conferma.

informazioni_personali = {"nome": "Mario", "cognome": "Rossi", "età": 27, "città": "Milano"}
print(type(informazioni_personali))
