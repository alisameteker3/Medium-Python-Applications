

sayi = int(input('sayi: '))

asalmı=True

if (sayi == 1):
    asalmı==False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmı=False
        break

if asalmı:
    print('sayi asaldir.')
else:
    print('sayi asal degildir.')

