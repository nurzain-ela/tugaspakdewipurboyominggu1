def cetak_pola_bintang_nol(baris):
    total_kolom = baris + 1
    for i in range(1, baris + 1):
        bintang = "*" * i
        nol = "0" * (total_kolom - i)
        print(bintang + nol)

cetak_pola_bintang_nol(6)