class ProstorZaTeret(object):
    def __init__(self, naziv, duzina, sirina, visina, roba = {}):
        self.naziv = naziv
        self.duzina = float(duzina) 
        self.sirina = float(sirina) 
        self.visina = float(visina) 
        self.roba = roba
        