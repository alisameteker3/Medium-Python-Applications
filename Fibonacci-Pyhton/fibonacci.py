n=int(input("n değeri giriniz: "))

while n<0:
    n=int(input("0'dan büyük n değeri giriniz: "))

a1=1
a2=1

if  n==1:
    print(a1)
elif n==2:
    print(a1,a2)
else:    
    print(a1,a2, end=" ")
    for i in range(2,int(n)):
        a3=a1+a2
        a1=a2
        a2=a3
        print(a3, end=" ")  