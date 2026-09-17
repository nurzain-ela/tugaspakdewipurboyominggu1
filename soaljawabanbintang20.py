def cetak_pola_berulang(baris, kolom):
    for i in range(baris):
        sisa_bagi = i % 3
        if sisa_bagi == 0:
            print("0" * kolom)
        elif sisa_bagi == 1:
            print("*" * kolom)
        elif sisa_bagi == 2:
            print("=" * kolom)
cetak_pola_berulang(6, 7)