def cetak_segitiga(n):
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

cetak_segitiga(5)