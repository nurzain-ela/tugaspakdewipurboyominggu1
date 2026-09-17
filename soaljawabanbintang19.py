def cetak_bingkai_kotak(baris, kolom):
    print("0" * kolom)
    for i in range(baris - 2):
        bintang_tengah = "*" * (kolom - 2)
        print("0" + bintang_tengah + "0")
    print("0" * kolom)
cetak_bingkai_kotak(6, 7)