def cetak_pola_biru(baris, kolom):
    WARNA_BIRU = "\033[94m"
    RESET_WARNA = "\033[0m"
    for i in range(baris - 1):
        teks_baris = ("*" * (kolom - 1)) + "0"
        print(WARNA_BIRU + teks_baris + RESET_WARNA)
    teks_bawah = "0" * kolom
    print(WARNA_BIRU + teks_bawah + RESET_WARNA)

cetak_pola_biru(6, 11)