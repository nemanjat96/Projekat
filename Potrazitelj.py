class Potrazitelj(Korisnik):
    def __init__(self, id, tip, ime, prezime, brojtelefona, email):
        super(Potrazitelj, self).__init__(ime, prezime, id, tip)
        self.brojtelefona = brojtelefona
        self.email = email 
        