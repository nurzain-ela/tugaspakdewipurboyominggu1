def cetak_pola(n):
    print("*" * (2 * n - 1))
    for i in range(1, n):
        bintang = "*" * (n - i)
        spasi = " " * (2 * i - 1)
        print(bintang + spasi + bintang)

cetak_pola(6)