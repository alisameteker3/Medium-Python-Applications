
name = input("Enter name : ")
print("Hosgeldiniz... " + name)

gizli_kelime ="metalica"

tahmin_karakter= ""

can = 10

while can > 0 : 
    karakter_sayi = 0

    for karkter in gizli_kelime:

        if karkter in tahmin_karakter:
            print(karkter)
        else:
            print(" - ")
            karakter_sayi += 1
    if karakter_sayi == 0:
        print(" Kazandiniz tebrikler...")
        break

 
    tahmin = input("Bir harf tahmin et : ")
    tahmin_karakter += tahmin

    if tahmin not in gizli_kelime:
        can -= 1
        print("Yanliş tahmin ..!")
        print(f"Kalan {can} sayisi : ")

        if can == 0:
            print("Adam asildi...")
 





