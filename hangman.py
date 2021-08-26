import random
import pictures
import words
print(" 1 : Hayvanlar\n 2 : Şehirler \n 3 : Meyveler \n 4 : Sebzeler")
hngmn_rsmler = pictures.Hangman_resimler
def kategori(indx):
    if   indx == "1":
        kelime_listesi = words.Hayvanlar
    elif indx == "2":
        kelime_listesi = words.Şehirler
    elif indx == "3":
        kelime_listesi = words.Meyveler
    else: 
        kelime_listesi = words.Sebzeler
    return kelime_listesi
secilen_kelime = random.choice(kategori(input("Lütfen Kategori Seçimi Yapınız : "))).lower() # Kelime seçip tüm harfleri kücültüyor.
hak = 6
görüntü = "_" * len(secilen_kelime) # Kelimenin uzunluguna göre _ koyuyor.
for x in range(0,len(secilen_kelime)-1):
    while hak > 0:
        print(hngmn_rsmler[hak])
        tahmin = input("Bir harf tahmin et : ").lower() # Harf alıp kücültüyor.
        while len(tahmin) >= 2 or tahmin.isalpha() == False:
            print("Lütfen sadece tek bir harf girisi yapınız !")
            tahmin = input("Bir harf tahmin et : ").lower()
        n = -1
        k = 0
        for harf in secilen_kelime :
            n +=1
            if harf == tahmin:
                görüntü = görüntü[:n] + tahmin + görüntü[n+1:] # Kelime icinde gezinip harf ile tahminin aynı oldugu noktalarda görüntümüzü degistiriyor.
                k += 1
                if görüntü == secilen_kelime:
                    print("\nTebrikler, Cevabı Buldunuz.") # Tüm harfler dogru bilinirse tebrik edip döngüden cıkarıyor.
                    hak = -1
            else:
                continue
        print("\n" + "    " + görüntü.upper())
        if k > 0 :
            continue
        else: 
            hak -= 1
if hak == 0:
    print(hngmn_rsmler[0])
    print("Malesef Bilemedin :( " + "\n" + "Doğru Cevap -->  " + secilen_kelime.upper())  # Haklar tükenirse doğru cevabı söyleyip bitiriyor.
