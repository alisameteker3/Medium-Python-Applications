
import random

sayi = random.randint(1,100)

hak = 5
sayac=0

while hak > 0 :
    hak -= 1
    sayac +=1

    tahmin = int (input("Tahmin :"))

    if sayi == tahmin:
        print(f'tebrikler. {sayac}. defada bildiniz ')
        break
    elif sayi > tahmin:
        print("yukari")
    else:
        print("asağı")

    if hak == 0:
        print(f"hakkınız bitti . tutlan sayi : {sayi} ")

    

