def cetak_panah_kiri(n):
    offset = 6 
    for i in range(n, 0, -1):
        spasi = " " * (offset + (n - i))
        bintang = "*" * i
        print(spasi + bintang)
    for i in range(2, n + 1):
        spasi = " " * (offset + (n - i))
        bintang = "*" * i
        print(spasi + bintang)

cetak_panah_kiri(5)