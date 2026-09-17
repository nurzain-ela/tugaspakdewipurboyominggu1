def cetak_pola_gradasi_merah(baris):
    WARNA_MERAH = "\033[91m"
    RESET_WARNA = "\033[0m"
    for i in range(1, baris):
        bintang = "*" * i
        spasi = " " * (2 * (baris - i) - 1)
        print(WARNA_MERAH + bintang + spasi + bintang + RESET_WARNA)
    print(WARNA_MERAH + "*" * (2 * baris - 1) + RESET_WARNA)
cetak_pola_gradasi_merah(6)