class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        return f"{self.brend} {self.model} — {self.narx:,} so'm".replace(",", " ")

    def __eq__(self, other):
        if not isinstance(other, Telefon):
            return False
        return self.narx == other.narx


tel1 = Telefon("Samsung", "A54", 4500000)
tel2 = Telefon("Redmi", "Note 13", 4500000)

print(tel1)
print(tel2)
print("Narxlari tengmi?:", tel1 == tel2)