class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        print(f"Xodim: {self.ism}, Maosh: {self.maosh} so'm")


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        print(f"O'qituvchi: {self.ism}, Fan: {self.fan}, Maosh: {self.maosh} so'm")


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        print(f"Farrosh: {self.ism}, Qavat: {self.qavat}-qavat, Maosh: {self.maosh} so'm")



oqituvchi1 = Oqituvchi("Aziza", 5500000, "Matematika")
farrosh1 = Farrosh("Rustam", 3000000, 2)

oqituvchi1.malumot()
farrosh1.malumot()