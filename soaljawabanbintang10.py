def cetak_pola_panah(n):
    spasi_awal = "    "
    for i in range(n, 0, -1):
        print(spasi_awal + ("*" * i))
    for i in range(2, n):
        print(spasi_awal + ("*" * i))

cetak_pola_panah(6)