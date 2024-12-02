import random

olcham = 5
oyinchi_jon = 100
dushman_jon = 100
dushman_zarar = 20
xazina = (random.randint(0,olcham-1),random.randint(0,olcham-1))

class oyinchi:
    def __init__(self):
        self.jon = oyinchi_jon
        self.sumka = []
        self.joylashuv = (0,0)
    def yur(self,yonalish):
        y,x = self.joylashuv
        if yonalish == "tepa" and y>0:
            self.joylashuv = y-1,x
        elif yonalish == "past" and y<olcham-1:
            self.joylashuv = y+1,x
        elif yonalish == "chap" and y>0:
            self.joylashuv = y,x-1
        elif yonalish == "ong" and x<olcham-1:
            self.joylashuv = y,x+1

    def hujum(self,dushman):
        print("Alibobo dushmanga hujum qildi!")
        dushman.jon -= 30

    def buyum_olish(self,buyum):
        self.sumka.append(buyum)
        print(f"{buyum.name} buyumi olindi")

    def yangi_joylashuv(self,yangi_joylashuv):
        self.joylashuv = yangi_joylashuv

class dushman:
    def __init__(self,joylashuv):
        self.jon = dushman_jon
        self.zarar = dushman_zarar
        self.joylashuv = joylashuv

    def yur(self):
        y, x = self.joylashuv
        yonalish = random.choice(['tepa','past','ong','chap'])
        if yonalish == "tepa":
            self.joylashuv = y - 1, x
        elif yonalish == "past":
            self.joylashuv = y + 1, x
        elif yonalish == "chap":
            self.joylashuv = y, x - 1
        elif yonalish == "ong":
            self.joylashuv = y, x + 1
    def hujum_qil(self,oyinchi):
        oyinchi.jon -=self.zarar
        print(f"Dushman hujumi!!! Qolgan jon {oyinchi.jon}")

class buyum:
    def __init__(self,name,qollanma,tasir):
        self.name = name
        self.qollanma = qollanma
        self.tasir = tasir
    def buyumni_ishlat(self,oyinchi):
        print(f"{self.name} ishlatildi. ")
        if self.tasir == "davolash":
            oyinchi.jon +=20
        print(f'O`yinchi joni {oyinchi.jon}')

# oyin logikasi
def oyin_run():
    maydon = [[' ' for _ in range(olcham)] for _ in range(olcham)]
    xazina_joy = xazina
    maydon[xazina_joy[0]][xazina_joy[1]] = 'T'

    p1 = oyinchi()

    dushmanlar = [dushman((random.randint(0,olcham-1),random.randint(0,olcham-1))) for i in range(3)]

    buyumlar = (buyum('aptechka',"20 foiz jonni tiklaydi","davolash"),buyum('aptechka',"20 foiz jonni tiklaydi","davolash"))

    return maydon,p1,dushmanlar,buyumlar,xazina_joy

def oyinni_boshlash():
    maydon,p1,dushmanlar,buyumlar,xazina_joy = oyin_run()
    print(xazina_joy)
    while True:
        print(f"O`yinchi joylashuvi: {p1.joylashuv}, jon: {p1.jon}")

        yurish = input("Yurish(tepa,past,ong,chap)ga: ")

        p1.yur(yurish)

        for dushman in dushmanlar:
            if p1.joylashuv == dushman.joylashuv:
                print("Dushmanga yo`liqdingiz!!!")
                p1.hujum(dushman)
                dushman.hujum_qil(p1)
        for buyum in buyumlar:
            if p1.joylashuv == xazina_joy:
                print("Tabriklaymiz, siz xazinani topdingiz va yutdingiz!!!")
                return
            if p1.jon <0:
                print('Afsuski joningiz tugadiva siz yutqazdingiz.')
                return
if __name__ == "__main__":
    oyinni_boshlash()