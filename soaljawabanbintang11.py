def cetak_pola_atap(baris, kolom):
    print("0" * kolom)
    for i in range(baris - 1):
        print("0" + "*" * (kolom - 1))

cetak_pola_atap(6, 11)