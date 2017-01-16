sayi_dizisi = [2,3,6,3,4,1,9,8,2,6 ]  # burda sayi_dizisi adi altinda sayilarimizi belirtiyoruz.

en_buyuk = -1                         # oncellikle en_buyuk sayi olarak -1 veriyoruz
for i in sayi_dizisi:                 # for loop ile sayi_dizisi'nin icindeki butun sayilara tek tek ulasiyoruz (i) degeri olarak
  if i > en_buyuk:                    # sayi_dizisi'deki her bir sayi'yi en_buyuk sayidan buyuk olup olmadagini sorguluyoruz
    en_buyuk = i                      # eger buyuk ise o sayi'yi en_buyuk olarak kaydetip, sayi_dizisindeki ikinci sayi icin ayni for loop baslicak

print("en buyuk sayi: {}".format(en_buyuk))
