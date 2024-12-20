# Listeler []

Renkler = ["Siyah" , "Sarı" , "Pembe" , "Yeşil" , "Turuncu"]

print(Renkler)

print(len(Renkler)) # Listeyi sayar

print(Renkler[1]) # 1. indeksteki elemanı verir.

print(Renkler[3])

print(Renkler[15]) # İndekste olmayan sırayı veremez.

print(Renkler[2:]) # 2. indeksten başlar sona kadar yazdırır.

print(Renkler[3:5]) # 3 den başlar 5 dahil yazdırır.

print(Renkler[::2]) # 2'şer olarak yazdırır.

# Metodlar

Renkler.append("Gri") # Listeye ekleme yapabilirsin.

Renkler.insert(2,"Lacivert") # İstediğin sıradaki indekse ekleme yapar.

Renkler.remove("Sarı") # Eleman silmeye yarar.

Renkler1 = ["Şarap" , "Viski" ,"Rakı"]

Renkler.extend(Renkler1) # Listeye ekleme yaptırır çoklu ekleme

print(Renkler),

Silinen = Renkler.pop() # Listeden sonuncu elemanı siler

print(Silinen)

Renkler.reverse()

print(Renkler) # Listeyi tersten yazdırır.

Renkler.sort() # Listeyi alfabetik olarak sıralar. Sayı varsa numerik sıralar.

print(Renkler)

Sayilar = [1,2,5,6,8,99,12,18,66,35,78,42]

print(min(Sayilar))

print(max(Sayilar))

print(sum(Sayilar))

for Sayi in Sayilar:  # For döngüsü tamamlayınca biter
    print(Sayi) 
    
print(enumerate(Sayilar))

print(list(enumerate(Renkler)))

print( "Gri" in Renkler)   # Varlığını kontrol ediyoruz.

StringRenkler = " ".join(Renkler)
print(StringRenkler)

StringRenkler1 = StringRenkler.split("-") # Her karakteri parçalayıp hepsine ayrı liste yapar.

print(StringRenkler1)
