def cetak_sudut_kanan_atas(baris, kolom):
    print("0" * kolom)
    for i in range(baris - 1):
        print("*" * (kolom - 1) + "0")

cetak_sudut_kanan_atas(6, 11)