import random
import time


class Giybet():
    def __init__(self, itiraf, oku):
        self.itiraf = itiraf
        self.oku = oku

    def itiraf_et(self):
        edilen_itiraf = input("itiraf et: ")
        self.oku.append(edilen_itiraf)
        print("itiraf gıybet kazanında")
        time.sleep(1)

    def okumak(self):
        print("Gıybet geliyor...")
        time.sleep(1)

        return print(random.choices(self.oku))


giybet = Giybet("itiraf", ["deneme1"])
hak = 0
sifre = "123456"
while True:
    x = input("""   ******************
     GIYBET KAZANI
     1-İtiraf ET
     2- Gıybet Oku 
   ******************
   """)

    if hak > 0:
        if x == "1":
            giybet.itiraf_et()
            hak += 1


        elif x == "2":
            giybet.okumak()
            hak -= 1

        else:
            print("hatalı işlem")
    elif hak == 0:
        y = input("itiraf yaz hak kazan 1 e bas \n 2 ye bas Kod kullan: ")

        if y == "1":
            giybet.itiraf_et()
            hak += 1

        elif y == "2":

            while True:
                kod = input("kod yaz: ")
                if sifre == kod:
                    hak += 2
                    print("güncel hak :" + str(hak))
                    break
                else:
                    print("hatalı kod")
                    continue