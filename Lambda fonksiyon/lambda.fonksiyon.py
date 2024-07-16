

def multiplay(a):
    return a**2

print(multiplay(4))

print("*"*50)

sonuc = (lambda a: a**2)(3)

print(sonuc)
print("*"*50)


sonuc = multiplay(5)

toplama = lambda a,b,c: a+b+c

sonuc = toplama(1,4,7)

tersCevir = lambda s: s[::-1]

sonuc = tersCevir("sadik")

print(sonuc)
print("*"*50)


def myFunc(n):
    return lambda a: a*n

multiplay2 = myFunc(2)

sonuc = multiplay2(10)

print(sonuc)

