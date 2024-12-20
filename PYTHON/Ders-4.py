# Demet ve Kümeler

Demet = ("Sarı" , "Mavi" , "Yeşil")

print(Demet) # Demetler değiştirilemez ve silinemez.

Kume = {"Sarı" , "Mavi" , "Yeşil"}
# Sırasız bir eleman yapısı vardır.

print(Kume)
print(Kume)
print(Kume)
print(Kume)

Kume.add("Pembe") # Ekleme yaptık.
print(Kume)

Kume.remove("Mavi") # Silme İşlemi olmayan işlemi silemez
print(Kume)

Kume.remove("Gri")
print(Kume) # hata verir

Kume.discard("Gri") # Gri silemez ama hata da vermez
