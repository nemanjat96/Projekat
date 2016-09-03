class Roba(object):
    def __init__(self, oznaka, naziv, opis, duzina, sirina, visina, tezina, potrazitelj):
        self.oznaka = int(oznaka)
        self.naziv = naziv
        self.opis = opis
        self.duzina = float(duzina) 
        self.sirina = float(sirina)
        self.visina = float(visina) 
        self.tezina = float(tezina)
        self.potrazitelj = id
        