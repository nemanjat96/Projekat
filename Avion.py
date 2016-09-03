class Avion(object):
    def __init__(self, oznaka, naziv, godiste, duzina, rasponKrila, visina, ukupnaNosivost, prostorZaTeret, relacija):
        self.oznaka = oznaka
        self.naziv = naziv
        self.godiste = int(godiste)
        self.duzina = float(duzina)
        self.rasponKrila = float(rasponKrila)
        self.visina = float(visina)
        self.ukupnaNosivost = float(ukupnaNosivost)
        self.relacija = relacija
        self.prostorZaTeret = prostorZaTeret
        