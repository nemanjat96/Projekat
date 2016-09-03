class ZahtevZaTransport(object):
    def __init__(self, id , potrazitelj , datumZahteva, datumTransporta, odrediste, avion, status = 0, roba = {}):
        self.id = int(id)
        self.potrazitelj = potrazitelj
        self.datumZahteva = datumZahteva
        self.datumTransporta = datumTransporta
        self.odrediste = odrediste
        self.avion = avion
        self.status = status
        self.roba = roba
        