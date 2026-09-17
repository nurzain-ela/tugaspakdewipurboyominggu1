def cetak_pola_gradasi_merah(baris):
    WARNA_MERAH = "\033[91m"
    RESET_WARNA = "\033[0m"
    total_kolom = baris + 1
    for i in range(1, baris + 1):
        nol = "0" * i
        bintang = "*" * (total_kolom - i)
        teks_baris = nol + bintang
        print(WARNA_MERAH + teks_baris + RESET_WARNA)

cetak_pola_gradasi_merah(6)