class Karta:
    def __init__(self, egasi, karta_nomi, balans):
        self.egasi = egasi
        self.karta_nomi = karta_nomi
        self.balans = balans

    def __str__(self):
        return f"Karta egasi: {self.egasi} ({self.karta_nomi}) | Balans: {self.balans:,} so'm".replace(",", " ")

    def __gt__(self, other):
        return self.balans > other.balans

    def __lt__(self, other):
        return self.balans < other.balans


karta1 = Karta("Sardor", "Humo", 2400000)
karta2 = Karta("Dilnoza", "Uzcard", 3850000)

print(karta1)
print(karta2)

if karta1 > karta2:
    print(f"Mablag' ko'p: {karta1.egasi}")
elif karta2 > karta1:
    print(f"Mablag' ko'p: {karta2.egasi}")
else:
    print("Ikkala kartada ham mablag' teng.")