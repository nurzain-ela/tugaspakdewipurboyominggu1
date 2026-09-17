def cetak_gabungan(n):
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        bintang = "*" * i
        print(spasi + bintang)

cetak_gabungan(3)