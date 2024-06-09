
def karsilastirma(a,b):
    if (a>b):
        return "a b den büyük"
    elif(b>a):
        return "b a dan büyük"
    else:
        "a b ye eşit"

sonuc = karsilastirma(10,20)
print(sonuc)

print("/"*50)


def karaktersayisi(string):
    return {letter: string.count(letter) for letter in string }

sonuc = karaktersayisi("python")
print(sonuc)

print("/"*50)

def update_list(liste, command, position, value=None):
    if ( command == "remove" and position == "end"):
        return liste.pop()
    elif(command == "remove" and position == "end"):
        return liste.pop(0)
    elif (command == "add" and position == "end"):
        liste.append(value)
        return liste
    elif(command == "add" and position == "beginning"):
        liste.insert(0,value)
        return liste


sonuc = update_list([1,2,3],"add","end","4")
sonuc = update_list([1,2,3],"add","beginning","4")
sonuc = update_list([1,2,3],"add","remove")

print(sonuc)

print("/"*50)

def contains_blue(*args):
    if "blue" in args:
        return True
    return False

sonuc = contains_blue("blue","green","black")
print(sonuc)








