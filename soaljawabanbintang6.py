def cetak_gabungan_2(n):
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        bintang = "*" * i
        print(spasi + bintang)
    for i in range(1, n + 1):
        print("*" * i)

cetak_gabungan_2(3)