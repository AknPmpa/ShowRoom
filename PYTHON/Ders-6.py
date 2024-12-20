# if - else Yapısı

if True:
    print("Koşul Doğru")
    print("Halen İf Bloğunun İçindeyiz")
    
if False:
    print("Bu Blok Yazılmaz")
    
a = 5
b = 5  
if a == b:
    print("Bu Yazar")
    
c = 10
d = 15   
if c == d:
    print("Görmez =")

c = 10
d = 15   
if c != d:
    print("Görür !=")
    
a = 6
b = 8

if a == b : # Koşul Gerçekleşir İse Bu Yapılır
    print("a = b")
else :
    print("a != b") # Koşul Gerçekleşmez İse Bu Yapılır
    
renk = "Siyah"

if renk == "Beyaz":
    print("Beyaz")
elif renk == "Sarı":
    print("Sarı")
elif renk == "Mavi":
    print("Mavi")
else:
    print("Hiçbiri")
    
renk = "Sarı"

if renk == "Beyaz":
    print("Beyaz")
elif renk == "Sarı":
    print("Sarı")
elif renk == "Mavi":
    print("Mavi")
else:
    print("Hiçbiri")
    
a = 5
b = 8
c = 10

if a < b or c > a :
    print("Koşul Doğru")
else:
    print("Koşul Yanlış")
    
Liste = [1,2,3,4,5,6,7,8,9,10]

a = 5
b = "ramazan"
if a and b in Liste:
    print("Listede Var")
else:
    print("Yok Lan Yok")