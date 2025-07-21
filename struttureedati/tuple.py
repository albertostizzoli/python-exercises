# LE TUPLE IN PYTHON

# 1): Creare una tupla vuota e assegnarla a una variabile.

tupla = ()
print(tupla)

# 2): Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".

tupla_frutta = ("mela", "banana", "kiwi")
print(tupla_frutta)

# 3): Accedere all'elemento "banana" della tupla precedente.

tupla_frutta = ("mela", "banana", "kiwi")
banana = tupla_frutta[1]
print(banana)

# 4): Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.

tupla_frutta = ("mela", "banana", "kiwi")
nuova_tupla = tupla_frutta[0:2]
print(nuova_tupla)

# 5): Verificare se l'elemento "ananas" è presente nella tupla precedente.

tupla_frutta = ("mela", "banana", "kiwi")
if "ananas" in tupla_frutta:
    print("L'ananas c'è nella tupla")
else:
    print("L'ananas non c'è nella tupla")

# 6): Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").

tupla_frutta = ("mela", "banana", "kiwi")
seconda_tupla_frutta = ("pesca", "arancia")

tupla_concatenata = tupla_frutta + seconda_tupla_frutta
print(tupla_concatenata)

# 7): Verificare la lunghezza della tupla precedente.

tupla_frutta = ("mela", "banana", "kiwi")
seconda_tupla_frutta = ("pesca", "arancia")

tupla_concatenata = tupla_frutta + seconda_tupla_frutta
lunghezza = len(tupla_concatenata)
print(tupla_concatenata)
print(lunghezza)

# 8): Creare una tupla contenente i numeri interi da 1 a 5.

numeri = (1, 2, 3, 4, 5)

print(numeri)

# 9): Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.

numeri_quadrati = tuple(x ** 2 for x in range(1, 6))

print(numeri_quadrati)

# 10): Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

tupla_frutta = ("mela", "banana", "kiwi")
conteggio = tupla_frutta.count("mela")
print(conteggio)

# 11): Creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari

parole = ("ciao", "alberto", "come", "stai")

for parola in parole:
    if len(parola) % 2 == 0:
        print(parola)

# 12): Creare una lista di tuple, in cui ogni tupla contiene due stringhe. 
# Stampare le tuple in cui la prima stringa inizia con la lettera “a”

lista_tuple = [("anna", "luca"), ("marco", "edoardo"), ("leonardo", "attilio")]

for tupla in lista_tuple:
    if tupla[0][0] == "a":
        print(tupla)

