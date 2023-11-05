urunList = {
    "elma": 4,
    "armut": 2,
    "kayisi": 5,
}

sepet = []

while True:
    eklenenUrun = input("Eklemek istediğiniz ürünü girin (Çıkmak için 'q' tuşuna basın): ")
    if eklenenUrun.lower() == 'q':
        break

    if eklenenUrun in urunList:
        for urun in urunList:
            if urun == eklenenUrun and urunList[urun] > 0:
                sepet.append(urun)
                urunList[urun] -= 1
                if urunList[urun] == 0:
                    del urunList[urun]
                print("Ürün sepete eklendi.")
                break
        else:
            print("Üzgünüz, bu ürün stokta kalmamıştır.")
    else:
        print("Üzgünüz, bu ürün mevcut değildir.")

print("Sepetinizdeki ürünler:", sepet)
