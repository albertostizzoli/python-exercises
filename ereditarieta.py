# EREDITARIETÀ IN PYTHON

# 1): Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. 
# Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da Veicolo 
# ma aggiunge la proprietà colore ed il metodo cambia_colore().

class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def accelera(self):
        print("Sto accelerando...")
    
    def frena(self):
        print("Sto frenando...")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore
    
    def cambia_colore(self, nuovo_colore):
        print(f"Cambio colore da {self.colore} a {nuovo_colore}")
        self.colore = nuovo_colore

mia_auto = Auto("Fiat", "Panda", 2020, "Rosso")
print(f"Auto: {mia_auto.marca} {mia_auto.modello}, Anno: {mia_auto.anno}, Colore: {mia_auto.colore}")

mia_auto.accelera()
mia_auto.frena()
mia_auto.cambia_colore("Blu")
print(f"Nuovo colore: {mia_auto.colore}")

# 2): Modifica la classe Auto in modo che erediti anche il metodo str() dalla classe Veicolo, 
# in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”.

class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def accelera(self):
        print("Sto accelerando...")
    
    def frena(self):
        print("Sto frenando...")
        
    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}"

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore
    
    def cambia_colore(self, nuovo_colore):
        print(f"Cambio colore da {self.colore} a {nuovo_colore}")
        self.colore = nuovo_colore

    def __str__(self):
        return super().__str__() + f", Colore: {self.colore}"

mia_auto = Auto("Ferrari", "Enzo", 2004, "Rosso")
print(mia_auto)  

mia_auto.accelera()
mia_auto.frena()
mia_auto.cambia_colore("Blu")
print(mia_auto) 

# 3): Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. 
# Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() 
# in modo appropriato per ogni forma. Utilizza le classi create per creare un quadrato e un cerchio, 
# quindi stampa l’area di ognuno di essi

import math

class Forma:
    def area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

quadrato = Quadrato(5)
print(quadrato.area())

cerchio = Cerchio(5)
print(cerchio.area())