class Hayvon:
    def __init__(self, nomi, ovoz):
        self.nomi = nomi
        self.ovoz = ovoz

    def ovoz_ber(self):
        print(f"{self.nomi} ovoz chiqaryapti: {self.ovoz}")


class It(Hayvon):
    def __init__(self, nomi):
        super().__init__(nomi, "Vov-vov")

    def qoriqlash(self):
        print(f"{self.nomi} hovlini qo'riqlayapti.")


class Mushuk(Hayvon):
    def __init__(self, nomi):
        super().__init__(nomi, "Miyov")

    def mirillash(self):
        print(f"{self.nomi} xursand bo'lib mirillayapti.")



it1 = It("Rex")
mushuk1 = Mushuk("Mosh")

it1.ovoz_ber()
it1.qoriqlash()

mushuk1.ovoz_ber()
mushuk1.mirillash()