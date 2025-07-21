# LE COSTANTI IN PYTHON

# 1): Definire una costante per il valore di pi greco e usarla 
# per calcolare la circonferenza di un cerchio di raggio 5.

pi_greco = 3.14159
raggio = 5
circonferenza = 2 * pi_greco * raggio

print("la circonferenza del cerchio è di", circonferenza, "cm")

#2): Definire una costante per il valore della gravità terrestre 
# e usarla per calcolare il peso di un oggetto di massa 10 kg.

gravita_terrestre = 9.81
massa = 10
peso = massa * gravita_terrestre

print("il peso dell'oggetto è:", peso)

# 3): Definire una costante per il tasso di cambio euro-dollaro 
# e usarla per convertire 100 euro in dollari

tasso_cambio_euro_dollaro = 1.1
euro = 100
dollari = euro * tasso_cambio_euro_dollaro

print("100 euro in dollari sono:", dollari)

# 4): Definire una costante per la velocità della luce 
# e usarla per calcolare quanto tempo impiega la luce a percorrere 1.000.000 km.

velocita_luce = 299792458  # in metri al secondo
distanza = 1000000 * 1000  # convertiamo in metri
tempo = distanza / velocita_luce

print("La luce impiega", tempo, "secondi per percorrere 1.000.000 km")

# 5): Definire una costante per il numero di giorni in una settimana 
# e usarla per calcolare quante settimane ci sono in 365 giorni.

giorni_settimana = 7
giorni = 365
settimane = giorni / giorni_settimana

print("In 365 giorni ci sono:", settimane, "settimane")

# 6): Definire una costante per il numero di minuti in un'ora 
# e usarla per calcolare quante ore ci sono in 720 minuti.

minuti_ora = 60
minuti = 720
ore = minuti / minuti_ora

print("In 720 minuti ci sono:", ore, "ore")

# 7): Definire una costante per il numero di giorni in un anno non bisestile 
# e usarla per calcolare quanti giorni ci sono in 5 anni non bisestili.

giorni_anno = 365
anni = 5
giorni_totali = anni * giorni_anno

print("In 5 anni ci sono", giorni_totali, "giorni")

# 8): Definire una costante per il valore di Planck 
# e usarla per calcolare l'energia di un fotone con una frequenza di 5e14 Hz.

costante_planck = 6.62607015e-34  # in joule per secondo
frequenza = 5e14  # in Hz
energia = costante_planck * frequenza

print("L'energia del fotone è:", energia, "joule")

# 9): Definire una costante per il numero di secondi in un'ora 
# e usarla per convertire 5 ore in secondi.

secondi_ora = 3600
ore = 5
secondi = ore * secondi_ora

print("In 5 ore ci sono", secondi, "secondi")

# 10): Definire una costante per il numero di centimetri in un metro 
# e usarla per convertire 250 centimetri in metri.

centimetri_metro = 100
centimetri = 250
metri = centimetri / centimetri_metro
print("250 centimetri sono", metri, "metri")
