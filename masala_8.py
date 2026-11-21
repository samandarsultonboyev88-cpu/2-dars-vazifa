class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        self.filmlar = list(filmlar) if filmlar is not None else []

    def film_qosh(self, film_nomi):
        self.filmlar.append(film_nomi)

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film_nomi):
        return film_nomi in self.filmlar


kutubxona1 = FilmKutubxonasi("Kino Olami")
kutubxona1.film_qosh("Inception")
kutubxona1.film_qosh("Interstellar")
kutubxona1.film_qosh("Dune")

kutubxona2 = FilmKutubxonasi("Klassik Kinolar", ["Matrix", "Gladiator", "Avatar"])

print(f"{kutubxona1.nom}dagi filmlar soni:", len(kutubxona1))
print("1-indeksdagi film:", kutubxona1[1])
print("'Dune' bormi?:", "Dune" in kutubxona1)

print(f"{kutubxona2.nom}dagi filmlar soni:", len(kutubxona2))
print("0-indeksdagi film:", kutubxona2[0])
print("'Titanic' bormi?:", "Titanic" in kutubxona2)