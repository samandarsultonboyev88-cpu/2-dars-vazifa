class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Kitob: '{self.nom}', Muallif: {self.muallif}, Sahifalar: {self.sahifa_soni}")


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format_turi, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format_turi = format_turi
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        print(
            f"Elektron kitob: '{self.nom}', Muallif: {self.muallif}, "
            f"Sahifalar: {self.sahifa_soni}, Format: {self.format_turi}, Hajmi: {self.fayl_hajmi} MB"
        )


kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 320)
ekitob1 = ElektronKitob("Clean Code", "Robert Martin", 464, "PDF", 12.5)

kitob1.malumot()
ekitob1.malumot()