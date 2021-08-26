import random
import pictures
import words

print(" 1 : Hayvanlar\n 2 : Sehirler \n 3 : Meyveler \n 4 : Sebzeler")

hngmn_rsmler = pictures.Hangman_resimler

def kategori(indx):    # Kategori Seçimi İçin Fonksiyon
    if   indx == "1":
        lst = words.Hayvanlar
    elif indx == "2":
        lst = words.Sehirler
    elif indx == "3":
        lst = words.Meyveler
    else: 
        lst = words.Sebzeler
    return lst

tercih = input("Lütfen Kategori Seçimi Yapınız : ") # Kategori için kullanıcı girdisi alıyor.

while tercih not in ["1","2","3","4"]:  
    print("Lütfen Sadece 1,2,3 veya 4 rakamını tuşlayın ! ")  # Kullanıcının kategori numarası haricinde birsey
    tercih = input("Lütfen Kategori Seçimi Yapınız : ")       # yazması durumunda tekrar sorgulama yapıyor.

secilen_kelime = random.choice(kategori(tercih)).lower() # Kelime seçip tüm harfleri kücültüyor.      

hak = 6 # Kullanıcının tahmin hakkı.

görüntü = "_" * len(secilen_kelime) # Kelimenin uzunluguna göre _ koyuyor.

for x in range(0,len(secilen_kelime)-1):   
    
    while hak > 0:       
        print(hngmn_rsmler[hak])
        tahmin = input("Bir harf tahmin et : ").lower() # Harf alıp kücültüyor.

        while len(tahmin) >= 2 or tahmin.isalpha() == False:
            print("Lütfen sadece tek bir harf girisi yapınız !")  # Kullanıcının tek harf harici birsey yazması
            tahmin = input("Bir harf tahmin et : ").lower()       # durumunda tekrar sorgulama yapıyor.
       
        n = -1  # Doğru tahmin edilen harfleri eklemek icin degisken.
        k = 0   # Dogru tahmin durumunda hakkın gitmememesi icin degisken.
 
        for harf in secilen_kelime :
            n +=1
 
            if harf == tahmin:
                görüntü = görüntü[:n] + tahmin + görüntü[n+1:] # Kelime icinde gezinip harf ile tahminin aynı oldugu noktalarda görüntümüzü degistiriyor.
                k += 1
 
                if görüntü == secilen_kelime:
                    print("\nTebrikler, Cevabı Buldunuz.") # Tüm harfler dogru bilinirse tebrik edip
                    hak = -1                               # döngüden cıkarıyor.
            else:
                continue
 
        print("\n" + "    " + görüntü.upper() + "\n")
 
        if k > 0 :
            continue    # Tahmin doğruysa devam ediliyor.
        else:           
            hak -= 1    # Yanlışsa hakkımız bir azalıyor.

if hak == 0:
    print(hngmn_rsmler[0])
    print("Malesef Bilemedin :( " + "\n" + "Doğru Cevap -->  " + secilen_kelime.upper())  # Haklar tükenirse doğru cevabı söyleyip bitiriyor.
