class Shakl:
    def yuza(self):
        return 0


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2


class TogriTortburchak(Shakl):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi


shakllar = [Kvadrat(6), TogriTortburchak(4, 7)]
for shakl in shakllar:
    print(f"{shakl.__class__.__name__} yuzasi: {shakl.yuza()}")