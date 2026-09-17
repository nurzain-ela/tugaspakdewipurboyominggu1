def cetak_segitiga_terbalik(n):
    for i in range(n, 0, -1):
        spasi = " " * (n - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

cetak_segitiga_terbalik(6)