# LE ECCEZIONI IN PYTHON

# 1): Scrivere un programma che tenta di dividere 10 per un numero 
# inserito dall'utente, gestendo l'errore se l'utente inserisce 0.

try:
    numero = int(input("Inserisci un numero: "))
    risultato = 10 / numero
    print("Il risultato è:", risultato)
except ZeroDivisionError:
    print("Errore: Non è possibile dividere per zero.")


# 2): Scrivere un programma che converte una stringa in un numero 
# intero e gestisce l'eccezione se la stringa non è un numero valido.

try:
    numero = int(input("Inserisci un numero: "))
    print("Il numero inserito è:", numero)
except ValueError:
    print("Errore: Inserito un valore non numerico.")


# 3): Scrivere un programma che accede a un indice di una lista 
# e gestisce l'eccezione se l'indice è fuori dai limiti della lista

lista = [1, 2, 3, 4, 5]
try:
    indice = int(input("Inserisci l'indice: "))
    print(lista[indice])
except IndexError:
    print("Errore: Indice fuori dai limiti.")


# 4): Scrivere un programma che apre un file per la lettura 
# e gestisce l'eccezione se il file non esiste.

try:
    with open("file_non_esistente.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Errore: File non trovato.")


# 5): Scrivere un programma che tenta di eseguire un'operazione
#  non supportata, come la divisione di due stringhe, e gestisce l'eccezione risultante.

try:
    '10' / '2'
except TypeError:
    print("Errore: Operazione non supportata tra stringhe.")


# 6): Scrivere un programma che tenta di convertire una stringa 
# in un tipo di dato non appropriato, gestendo l'eccezione.

stringa = "testo_non_numerico"

try:
    numero = float(stringa)
    print("Conversione riuscita:", numero)
except ValueError:
    print("Errore: Conversione non valida.")


# 7): Scrivere un programma che chiede all'utente di inserire 
# un valore e tenta di usarlo come indice per una lista vuota, gestendo l'errore.

lista_vuota = []

try:
    indice = int(input("Inserisci un indice: "))
    print("Elemento alla posizione richiesta:", lista_vuota[indice])
except IndexError:
    print("Errore: Indice non valido per una lista vuota.")
except ValueError:
    print("Errore: Devi inserire un numero intero.")


# 8): Scrivere un programma che tenta di chiamare un metodo inesistente 
# su un oggetto, gestendo l'eccezione risultante.

try:
    oggetto = {}
    oggetto.metodo_inesistente()
except AttributeError:
    print("Errore: Metodo non esistente.")


# 9): Scrivere un programma che prova a leggere un file e chiude 
# il file indipendentemente dal risultato dell'operazione, usando finally.

try:
    file = open("esempio.txt", "r")
    contenuto = file.read()
    print(contenuto)
except FileNotFoundError:
    print("Errore: File non trovato.")
finally:
    file.close()
    print("File chiuso.")


# 10): Scrivere un programma che chiede all'utente di inserire un numero 
# e divide 100 per quel numero, stampando un messaggio in un blocco finally.

try:
    numero = int(input("Inserisci un numero: "))
    risultato = 100 / numero
    print("Il risultato della divisione è:", risultato)
except ZeroDivisionError:
    print("Errore: Divisione per zero.")
finally:
    print("Operazione di divisione tentata.")


# 11): Scrivere un programma che gestisce più tipi di eccezioni in un solo blocco 
# except e utilizza un blocco finally per mostrare un messaggio di fine operazione.

try:
    valore = int(input("Inserisci un valore: "))
    print(10 / valore)
except (ValueError, ZeroDivisionError) as e:
    print("Errore:", e)
finally:
    print("Tentativo di calcolo completato.")


# 12): Scrivere un programma che prova ad aggiungere un elemento a un tuple,
#  mostrando un messaggio nel blocco finally.

try:
    tupla = (1, 2, 3)
    tupla[0] = 4
except TypeError:
    print("Errore: Impossibile modificare una tupla.")
finally:
    print("Modifica di tupla tentata.")


# 13): Scrivere un programma che chiede all'utente di inserire un numero, 
# convertendolo in intero, e usa finally per confermare l'input ricevuto.

try:
    numero = int(input("Inserisci un numero: "))
    print("Numero inserito:", numero)
except ValueError:
    print("Errore: Devi inserire un valore numerico.")
finally:
    print("Controllo dell'input completato.")


# 14): Scrivere un programma che prova a calcolare l'inverso di un numero 
# dato dall'utente e stampa un messaggio in finally.

try:
    numero = float(input("Inserisci un numero: "))
    inverso = 1 / numero
    print("L'inverso del numero è:", inverso)
except ZeroDivisionError:
    print("Errore: Non è possibile calcolare l'inverso di zero.")
finally:
    print("Tentativo di calcolo dell'inverso effettuato.")


# 15): Scrivere un programma che tenta di aprire un file e leggere il suo contenuto,
#  con un messaggio finale che indica se il file era aperto o meno.

try:
    file = open("file_testo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Errore: File non trovato.")
finally:
    if not file.closed:
        file.close()
        print("File chiuso correttamente.")
    else:
        print("File già chiuso.")