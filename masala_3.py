class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda.")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda tez yurmoqda.")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal aylantirib ketmoqda.")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd temir yo'lda signal berib harakatlanmoqda.")


transportlar = [Mashina(), Velosiped(), Poyezd()]
for t in transportlar:
    t.harakatlanish()