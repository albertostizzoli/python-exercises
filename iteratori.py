# GLI ITERATORI IN PYTHON

# 1): Data una lista di numeri, crea un’iteratore che restituisca solo i numeri pari

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Pari:
    def __init__(self, numeri):
        self.numeri = numeri
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numeri):
            if self.numeri[self.index] % 2 == 0:
                valore = self.numeri[self.index]
                self.index += 1
                return valore
            else:
                self.index += 1
        raise StopIteration

iteratore_pari = Pari(numeri)

for numero in iteratore_pari:
    print(numero)

# 2): Data una stringa, crea un iteratore che restituisca ogni carattere della stringa in ordine inverso.

parola = "ciao"

class Inverso:
    def __init__(self, parola):
        self.parola = parola
        self.index = len(parola)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.parola[self.index]
        else:
            raise StopIteration

iteratore_inverso = Inverso(parola)

for carattere in iteratore_inverso:
    print(carattere)

# 3): Data una lista di parole, crea un iteratore che restituisca solo le parole che contengono una data lettera.

parole = ["casa", "cane", "gatto", "auto", "treno", "bicicletta"]
lettera = "a"

class ConLettera:
    def __init__(self, parole, lettera):
        self.parole = parole
        self.lettera = lettera
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.parole):
            if self.lettera in self.parole[self.index]:
                valore = self.parole[self.index]
                self.index += 1
                return valore
            else:
                self.index += 1
        raise StopIteration

iteratore_con_lettera = ConLettera(parole, lettera)

for parola in iteratore_con_lettera:
    print(parola)

# 4): Data una lista di numeri, crea un iteratore che restituisca la somma cumulativa dei numeri.

numeri = [1, 2, 3, 4, 5]

class Cumulativo:
    def __init__(self, numeri):
        self.numeri = numeri
        self.index = 0
        self.somma = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numeri):
            self.somma += self.numeri[self.index]
            self.index += 1
            return self.somma
        else:
            raise StopIteration

iteratore_cumulativo = Cumulativo(numeri)

for somma in iteratore_cumulativo:
    print(somma)

