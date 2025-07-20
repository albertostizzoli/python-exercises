# FUNZIONI LAMBDA IN PYTHON

# 1): Scrivi una lambda function che prenda un parametro e restituisca il quadrato del numero

quadrato = lambda x: x ** 2

print(quadrato(5))

# 2): Scrivi una lambda function che prenda una lista e restituisca una lista di tutti gli elementi 
# della lista originale moltiplicati per 2

lista = [1, 2, 3, 4, 5, 6]

moltiplica_per_due = lambda lista: [x * 2 for x in lista]

print(moltiplica_per_due(lista))

# 3): Scrivi una lambda function che prenda una lista di parole e restituisca una lista contenente 
# solo le parole che iniziano con la lettera “a”

lista = ["allora", "cane", "albero", "pollo", "treno"]

filtra_parole = lambda lista: [parola for parola in lista if parola.startswith("a")]

print(filtra_parole(lista))

# 4): Scrivi una lambda function che prenda due numeri e restituisca la somma dei loro quadrati

somma_quadrati = lambda x, y: x**2 + y**2

print(somma_quadrati(3, 4)) 

# 5): Scrivi una lambda function che prenda una stringa e restituisca True se la stringa è palindroma, altrimenti False.

s = "radar"
palindromo = lambda s: s == s[::-1]

print(palindromo(s))

# 6): Scrivi una lambda function che prenda una lista di parole e restituisca la lunghezza media delle parole nella lista.

lista = ["allora", "cane", "albero", "pollo", "treno"]
lunghezza_media = lambda lista: sum(len(parola) for parola in lista) / len(lista)

print(lunghezza_media(lista))

# 7): Scrivi una lambda function che prenda una lista di numeri e restituisca la somma solo dei numeri pari.

lista = [1, 2, 3, 4, 5, 6]
somma_pari = lambda lista: sum(x for x in lista if x % 2 == 0)

print(somma_pari(lista))

# 8): Scrivi una lambda function che prenda una lista di dizionari e restituisca una lista di tutte le chiavi dei dizionari.

tutte_le_chiavi = lambda lista: [chiave for dizionario in lista for chiave in dizionario.keys()]

lista_dizionari = [{'nome': 'Alice'}, {'età': 30}, {'città': 'Roma', 'paese': 'Italia'}]

print(tutte_le_chiavi(lista_dizionari))

# 9): Scrivi una lambda function che prenda una lista di numeri e restituisca una lista di tutti i numeri maggiori di 10.

numeri_maggiori_di_10 = lambda lista: [x for x in lista if x > 10]

lista_numeri = [4, 11, 8, 15, 3, 22]

print(numeri_maggiori_di_10(lista_numeri))

# 10): Scrivi una lambda function che prenda una lista di tuple e restituisca una 
# lista di tuple ordinate per il secondo elemento di ciascuna tupla.

ordina_per_secondo_elemento = lambda lista: sorted(lista, key=lambda tupla: tupla[1])

lista_di_tuple = [(1, 5), (2, 1), (3, 8), (4, 3)]

print(ordina_per_secondo_elemento(lista_di_tuple))