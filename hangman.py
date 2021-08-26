import random
Hangman_resimler = ['''
    +---+
        |
   DEAD |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
kelime_listesi = "Adapte,Adalet,Alerji,Aralık".split(",") # Kelime listesi.
secilen_kelime = random.choice(kelime_listesi).lower() # Kelime seçip tüm harfleri kücültüyor.
hak = 6
görüntü = "_" * len(secilen_kelime) # Kelimenin uzunluguna göre _ koyuyor.
for x in range(0,len(secilen_kelime)-1):
    while hak > 0:
        print(Hangman_resimler[hak])
        tahmin = input("Bir harf tahmin et : ").lower() # Harf alıp kücültüyor.
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
    print(Hangman_resimler[0])
    print("Malesef Bilemedin :( " + "\n" + "Doğru Cevap -->  " + secilen_kelime.upper())  # Haklar tükenirse doğru cevabı söyleyip bitiriyor.
