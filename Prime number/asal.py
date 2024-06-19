# Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan Python Örneği
sayi=input("Sayı giriniz: ")
sayac=0

for i in range(2,int(sayi)):
    if int(sayi)%i==0:
        sayac+=1

if int(sayac)>0:
    print("Sayı asal değildir.")
elif int(sayac)==0:
    print("Sayı asaldır.")    