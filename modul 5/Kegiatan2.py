import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk, jumlah_terjual = zip(*[(harga, jumlah) for _, harga, jumlah in data_transaksi])

# TODO 2: Buat Scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.scatter(harga_produk, jumlah_terjual, color='blue', label='Penjualan Produk')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')
plt.legend()
plt.show()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
produk_names = [produk for produk, _, _ in data_transaksi]
plt.bar(produk_names, pendapatan_produk, color='blue', label='Pendapatan Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk')
plt.title('Pendapatan Produk')
plt.legend()
plt.show()
