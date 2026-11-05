#No 1 kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Menambahkan truk di akhir list
kendaraan.append('truk')
print("a. Menambah Kendaraan:", kendaraan)
# b. Menyisipkan becak pada index ke-1 yaitu setelah motor
kendaraan.insert(1, 'becak')
print("b. Menyisipkan becak:", kendaraan)
# c. Menghapus data paling belakang
kendaraan.pop()
print("c. menghapus data kendaraan terakhir:", kendaraan)
# d. Mengubah sepeda menjadi skuter
kendaraan[3] = 'skuter'
print("d. mengubah sepeda menjadi skuter:", kendaraan)
# e. Menampilkan jumlah total data
print("e. Jumlah data:", len(kendaraan))


#No 2 angka = [75, 80, 90, 75, 85, 100, 65]
angka = [75, 80, 90, 75, 85, 100, 65]

# a. indeks nilai 100
print("a. Indeks nilai 100:", angka.index(100))
# b. jumlah nilai 75
print("b. Jumlah nilai 75:", angka.count(75))
# c. Mengurutkan nilai dari terkecil ke terbesar
angka.sort()
print("c. Urutan terkecil ke terbesar:", angka)
# d. Membalikkan urutan list
angka.reverse()
print("d. Urutan terbesar ke terkecil:", angka)


#No 3 Menggabungkan Menu Tambahan ke dalam menu Utama
menu_utama = ["Nasi Goreng", "Mie Ayam"]

# Menggabungkan kedua list
menu_tambahan = ["Kerupuk", "Es Teh"]
menu_utama.extend(menu_tambahan)
print(f"Menu gabungan: \n{menu_utama}")


#No 4 Nested List
data_barang = [["Buku", 5000],["Pensil", 2000],["Penggaris", 3000]]

# a. Menampilkan harga Pensil
print("a. Harga Pensil:", data_barang[1][1])
# b. Menampilkan seluruh data barang menggunakan perulangan
print("\nb. Data seluruh barang:")

for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")
