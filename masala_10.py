class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        self.mahsulotlar = list(mahsulotlar) if mahsulotlar is not None else []

    def qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat: '{self.nom}', Mahsulotlar soni: {len(self)}"


savat1 = Savat("Texnika savati")
savat1.qosh(Mahsulot("Sichqoncha", 120000))
savat1.qosh(Mahsulot("Klaviatura", 250000))
savat1.qosh(Mahsulot("Quloqchin", 310000))

savat2 = Savat("Bo'sh savat")

if savat1:
    print(savat1)
    print(f"Umumiy narx: {savat1.umumiy_narx():,} so'm".replace(",", " "))
else:
    print(f"'{savat1.nom}' bo'sh.")

if savat2:
    print(savat2)
    print(f"Umumiy narx: {savat2.umumiy_narx():,} so'm".replace(",", " "))
else:
    print(f"'{savat2.nom}' bo'sh.")