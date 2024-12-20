# Sözlük Nedir

Kişi = {"isim" : " Ali" , "Yas" : 20 , "Cinsiyet" : "M" , "Hobiler" : ["Sinema","Konser"]}

print (Kişi["Hobiler"]) # Erişme yöntemi

print(Kişi)

Kişi["isim"] = "Ahmet" # Sözlük İçerik Güncelleme
print(Kişi)

Kişi.update({"isim" : "Ramazan" , "Yas" : 27}) # Sözlük İçerik Güncelleme

print(Kişi)

Kişi["Id"] = 12345
print(Kişi)

del Kişi["Id"] # Silme İşlemine Yarıyor
print(Kişi)

for x in Kişi:
    print(Kişi[x])
    
print(Kişi.keys())

print(Kişi.items())

for k,v in Kişi.items():
    print(k,v)

