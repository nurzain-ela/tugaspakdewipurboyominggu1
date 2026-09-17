def cetak_pola_huruf_L(baris, kolom):
    for i in range(baris - 1):
        print("0" + "*" * (kolom - 1))
    print("0" * kolom)

cetak_pola_huruf_L(6, 11)