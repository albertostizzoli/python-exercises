# GLI OPERATORI MATEMATICI IN PYTHON

# 1): Dichiarare due variabili "numero1" e "numero2" e assegnargli due numeri interi. 
# Eseguire l'addizione tra le due variabili e assegnare il risultato 
# ad una nuova variabile "somma", mandandola a schermo.

numero1 = 5
numero2 = 3
somma = numero1 + numero2

print(somma)

# 2): Eseguire la sottrazione tra le due variabili 
# e assegnare il risultato ad una nuova variabile "differenza". Mandare a schermo.

numero1 = 5
numero2 = 3
differenza = numero1 - numero2

print(differenza)

# 3): Eseguire la moltiplicazione tra le due variabili 
# e assegnare il risultato ad una nuova variabile "prodotto". Mandare a schermo.

numero1 = 5
numero2 = 3
prodotto = numero1 * numero2

print(prodotto)

# 4): Eseguire la divisione tra le due variabili 
# e assegnare il risultato ad una nuova variabile "quoziente". Mandare a schermo.

numero1 = 10
numero2 = 2
divisione = int(numero1 / numero2)

print (divisione)

# 5): Eseguire l'operazione di modulo tra le due variabili 
# e assegnare il risultato ad una nuova variabile "resto". Mandare a schermo.

numero1 = 10
numero2 = 2
modulo = int(numero1 % numero2)

print (modulo)

# 6): Incrementare "numero1" di 1 e decrementare "numero2" di 3. Mandare a schermo i nuovi valori.

numero1 = 10
numero2 = 2

numero1 += 1
numero2 -= 3

print (numero1, numero2)

# 7): Moltiplicare "numero1" per se stesso + 5, sommarlo quindi a "numero2" elevato alla seconda. 
# Assegnare l'operazione alla variabile risultato e mandare a schermo.

numero1 = 10
numero2 = 5

numero1 = numero1 * (numero1 + 5)
risultato = numero1 + numero2 ** 2

print (risultato)

# 8): Trovare quella operazione per portare "numero1" a valere 1 senza riassegnarlo direttamente ad 1 e sottraendolo a se stesso.

numero1 = 10
numero2 = 5

numero1 = numero1 - (numero1 - 1)

print (numero1)
