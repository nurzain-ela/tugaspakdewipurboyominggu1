def cetak_pola_rjust(baris):
    total_kolom = baris + 1
    for i in range(1, baris + 1):
        bintang = "*" * i
        print(bintang.rjust(total_kolom, "0"))
cetak_pola_rjust(6)