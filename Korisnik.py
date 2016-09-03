class Korisnik(object):
    def __init__(self, ime, prezime, id, tip):
        self.ime = ime
        self.prezime = prezime
        self.id = int(id)
        self.tip = tip