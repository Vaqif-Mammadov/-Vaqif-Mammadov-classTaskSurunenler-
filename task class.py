class surunen():
    sinif ="Surunenler"

    def __init__(self, ad, olcu, reng):
        self.ad = ad
        self.olcu = olcu
        self.reng = reng

    def uze_bilme(self, uze_bilme=False):
        if uze_bilme:
            return f"{self.ad} uze bilir"
        else:
            return f"{self.ad} uze bilmir"

    def reng_deyise_bilme(self, reng_deyise_bilme=False ):
        if reng_deyise_bilme:
            return f"{self.ad} reng deyise bilir"
        else:
            return f"{self.ad} reng deyise bilmir"

    def uca_bilme(self, uca_bilme = False):
        if uca_bilme:
            return f"{self.ad} uca bilir"
        else:
            return f"{self.ad} uca bilmir"

timsah = surunen("Timsah", "6 metr", "qehveyi")
print(f"{timsah.ad}-in uzunlugu {timsah.olcu} -e qederdir")
print(timsah.uze_bilme(True))
print(timsah.reng_deyise_bilme())
print(timsah.uca_bilme())


tisbaga = surunen("Tisbaga", "30sm","qonur")
print(f"{tisbaga.ad}-nin uzunlugu {tisbaga.olcu} -e qederdir")
print(tisbaga.uze_bilme(True))
print(tisbaga.uca_bilme())
print(tisbaga.reng_deyise_bilme())

buqelemun=surunen("Buqelemun", "28sm", None)
print(f"{buqelemun.ad} -un uzunlugu {buqelemun.olcu}-dir")
print(buqelemun.uze_bilme())
print(buqelemun.uca_bilme())
print(buqelemun.reng_deyise_bilme(True))