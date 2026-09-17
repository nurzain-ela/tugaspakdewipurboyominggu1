def cetak_diagonal_biru(baris):
    WARNA_BIRU = "\033[94m"
    RESET_WARNA = "\033[0m"
    for i in range(baris):
        nol_depan = "0" * i
        bintang = "*"
        nol_belakang = "0" * (baris - i)
        teks_baris = nol_depan + bintang + nol_belakang
        print(WARNA_BIRU + teks_baris + RESET_WARNA)
cetak_diagonal_biru(6)