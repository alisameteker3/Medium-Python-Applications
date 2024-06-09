

AliHesap = {
    'ad': ' Ali Samet Eker',
    'hesapNo': '1234567',
    'bakiye': 3000,
    'ekHesap': 2000,

}


SametHesap = {
    'ad': 'Samet Eker',
    'hesapNo': '21234567',
    'bakiye': 2000,
    'ekHesap': 1000,

}

def paraCek(hesap , miktar ):
    print(f"merhaba {hesap['ad']}")
    if(hesap['bakiye'] >= miktar):
        kalanbakiye = hesap['bakiye'] - miktar
        print(f"cekilen tutariniz : {miktar}")   
        print(f"kalan bakiyeniz : {kalanbakiye}")
        print("Paranizi alabilrsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullaimi = input('ek hesap kullailsin mi (e/h)')
           # hesap['ekHesap'] -= ekHesapKullanicakmiktar
            if ekHesapKullaimi == 'e':
                ekHesapKullanicakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanicakmiktar
                print('paranizi alabilrisiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunaktadir")
            
        else:
            print("Üzgünüz bakiye yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limintiniz ise {hesap['ekHesap']} TL bulunamaktadir")


paraCek(AliHesap,3000)
bakiyeSorgula(AliHesap)
print("*"*50)

paraCek(AliHesap,4000)
 
 