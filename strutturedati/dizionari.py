# I DIZIONARI (DICT) IN PYTHON

# 1): Creare un dizionario vuoto e assegnarlo a una variabile.

mio_dizionario = {}

print(mio_dizionario)

# 2): Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}

print(persona)

# 3): Accedere al valore dell'elemento con chiave "età" del dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}


print(persona.get("età"))

# 4): Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}
persona["email"] = "mario.rossi@email.com"

print(persona)

# 5): Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}
del persona["cognome"]

print(persona)

# 6): Creare una nuova lista che contenga solo le chiavi del dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}
chiavi = list(persona.keys())

print(chiavi)

# 7): Creare una nuova lista che contenga solo i valori del dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}
valori = list(persona.values())

print(valori)

# 8): Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}

persona["età"] = 35

print(persona)

# 9): Contare il numero di elementi nel dizionario precedente.

persona = {
    "nome": "Mario", 
    "cognome": "Rossi", 
    "età": 30
}

num_elementi = len(persona)

print(num_elementi)

# 10): Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi. 
# Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5**

dizionario = {
    "chiave1": 10,
    "chiave2": 7,
    "chiave3": 5
}

for chiave, valore in dizionario.items():
    if valore > 5:
        print(chiave, valore)

