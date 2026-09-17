def cetak_garis_diagonal(baris):
    total_kolom = baris + 1
    for i in range(1, baris + 1):
        nol_depan = "0" * (total_kolom - i)
        bintang = "*"
        nol_belakang = "0" * (i - 1)
        print(nol_depan + bintang + nol_belakang)
cetak_garis_diagonal(6)