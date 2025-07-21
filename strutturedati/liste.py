# LE LISTE IN PYTHON

# 1): Creare una lista vuota e assegnarla a una variabile.

mia_lista = []
print(mia_lista)

# 2): Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.

lista_numeri = [1, 2, 3, 4, 5]
print(lista_numeri)

# 3): Accedere all'elemento con indice 2 della lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
terzo_elemento = lista_numeri[2]
print(terzo_elemento)


# 4): Aggiungere un nuovo elemento "6" alla lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
lista_numeri.append(6)
print(lista_numeri) 

# 5): Rimuovere l'elemento con indice 3 dalla lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
del lista_numeri[3]
print(lista_numeri)

# 6): Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
nuova_lista = lista_numeri[:3]
print(nuova_lista)

# 7): Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
dispari = lista_numeri[1::2]
print(dispari)

# 8): Ordinare la lista precedente in ordine decrescente.

lista_numeri = [1,2,3,4,5]
lista_numeri.sort(reverse=True) 
print(lista_numeri)

# 9): Contare quante volte l'elemento "2" appare nella lista precedente.

lista_numeri = [1, 2, 3, 4, 5]
count_2 = lista_numeri.count(2)
print(count_2) 

# 10): Creare una lista di numeri interi e stampare gli elementi che sono divisibili per 3

lista_numeri = [2, 3, 6, 9, 11, 14, 15]

for lista in lista_numeri:
    if lista % 3 == 0:
        print(lista)