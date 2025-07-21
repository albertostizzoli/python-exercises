# LE CLASSI IN PYTHON

# 1): Creare una classe Persona che abbia i seguenti attributi: NOME, ETA’, SESSO. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona. 
# Ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:
    def __init__(self, nome, età, sesso):
        self.nome = nome
        self.eta = età
        self.sesso = sesso
    
    def presentati(self):
        print(f"Ciao mi chiamo {self.nome} e sono un {self.sesso} di {self.eta} anni")
        
p = Persona("Marco", 32, "ragazzo")
p.presentati()

# 2): Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
# Ad esempio, se l’animale è un gatto dovrebbe essere “Miao!”, se è un cane “Bau!”

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    
    def emetti_suono(self):
        if self.specie == "Gatto":
            print("Miao!")
        elif self.specie == "Cane":
            print("Bau!")
        else:
            print("Non so che verso sia")
            
a = Animale("Leone", "Gatto")
a.emetti_suono()

b = Animale("Buddy", "Cane")
b.emetti_suono()

# 3): Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”.
#  Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, 
# ad esempio “Questa è una Toyota Corolla del 2017”.

class Automobile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrizione(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")

a = Automobile("Toyota", "Corolla", 2017)
a.descrizione()

# 4): Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” 
# che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio
    
    def aumenta_stipendio(self):
        self.stipendio *= 1.1
        
    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola: {self.matricola}, stipendio: {self.stipendio:.2f} Euro")

a = Impiegato("Marco", "Rossi", 12345, 3000)
a.stampa_dettagli()
a.aumenta_stipendio()
a.stampa_dettagli()

# **5): Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:**

#- **Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)**
#- **Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese**

#**La classe dovrà avere i seguenti metodi:**

#- **Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino**
#- **Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino**
#- **Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino**

#**Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.**

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

class GestoreMagazzino:
  def __init__(self, costo_magazzinaggio):
    self.prodotti = {}
    self.costo_magazzinaggio = costo_magazzinaggio

  def aggiungi_prodotto(self, prodotto):
    self.prodotti[prodotto.nome] = prodotto

  def rimuovi_prodotto(self, nome_prodotto):
    self.prodotti.pop(nome_prodotto)

  def calcola_costi_magazzinaggio(self):
    costi = 0
    for nome, prodotto in self.prodotti.items():
      costi += prodotto.scorta * self.costo_magazzinaggio
    return costi
p1 = Prodotto("Telefono", 500, 10)
p2 = Prodotto("Computer", 1000, 5)

gm = GestoreMagazzino(10)

gm.aggiungi_prodotto(p1)
gm.aggiungi_prodotto(p2)

print(gm.calcola_costi_magazzinaggio()) 

gm.rimuovi_prodotto("Telefono")

print(gm.calcola_costi_magazzinaggio())  