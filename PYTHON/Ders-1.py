# Print ile yazdırma

print("Merhaba Dünya") #Yazdırma İşleminde kullanırız.
print('Merhaba Misafir')
print("Ali'nin evi")
# \ Karatkeri kaçma işaretidir konduktan sonraki karakteri gizler.

# \n Yeni bir satır anlamına gelir
# \t Tab anlamına gelir boşluk bırakır
print("Merhaba \# Ramazan \t Geldim.")

Mesaj = "Ramazan Cesuroğlu"
Mesaj1 = "5379137005"
print(Mesaj + Mesaj1)

# String içindeki belirli bir harfi almak

print(Mesaj[1])
print(Mesaj[-2])
print(Mesaj[0:4]) # 0 Dahil 4'e kadar yaz (4 Hariç)

print(Mesaj[::2]) # 2'Şer giderek yazdırır.
print(Mesaj[::-1]) # Tersten yazdırır.

print(Mesaj.upper()) #.upper() fonk. büyük harf yapar.

print(Mesaj.lower()) #.lower() fon. küçük harf yapar.

print(Mesaj.capitalize()) #.capitalize() fonk. baş harf büyük yapar.

print(Mesaj.startswith("M")) #.startswith() + .endswith() başlama ve bitiş harf ve kelimeleri seçer.

İsim = "Ramazan"
Yas = 27
print("{} , {} yaşındadır." .format(İsim,Yas))

