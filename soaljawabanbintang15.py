def cetak_nol_bintang_kanan(baris):
    total_kolom = baris + 1   
    for i in range(1, baris + 1):
        nol = "0" * (total_kolom - i)
        bintang = "*" * i
        print(nol + bintang)
cetak_nol_bintang_kanan(6)