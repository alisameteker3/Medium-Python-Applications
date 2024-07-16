
sayilar= [1,2,5,7,9,-6,-1,-9]

str_sayilar = ["1","2","5","7","9"]

isimler = ["Ali","Veli","Deniz","Fatih"]

kareleri = []

kullanicilar = [
    {"ad": "ali", "soyad":"yilmaz"},
    {"ad": "ahmet", "soyad":"yilmaz"}

]


for sayi in sayilar:
    kareleri.append(sayi ** 2)


print(kareleri)

print("*"*50)

def kareAl(sayi):
    return sayi ** 2

sonuc = map(kareAl, sayilar)

kareleri.append

print(f"{kareleri} bunlardir")
print("*"*50)

sonuc = list(map(int, str_sayilar))
sonuc = list(map(abs, sayilar))
sonuc = list(map(float, str_sayilar))
sonuc = list(map(str.lower, isimler))
sonuc = list(map(str, isimler))
sonuc = list(map(lambda x: x["ad"], kullanicilar))

 
print(sonuc)
