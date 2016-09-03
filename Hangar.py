class Hangar(object):
    def __init__(self, oznaka, naziv, duzina, sirina, visina, avioni = []):
        self.oznaka = oznaka
        self.naziv = naziv
        self.duzina = float(duzina)
        self.sirina = float(sirina)
        self.visina = float(visina)
        self.avioni = avioni
        