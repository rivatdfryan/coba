# Nama        : Rivat Defryanto
# NIM         : 242410103050
# Mata Kuliah : Algoritma dan pemrograman 1 Kelas E

'''Soal 1
Diberikan beberapa list yang memiliki nilai berbeda-beda. Masukkan value dari list angka
ganjil dan angka genap ke dalam list yang masih kosong. Tetapi angka yang dimasukkan
ke dalam list harus memiliki selisih 3. Selain itu, angkanya juga harus urut mulai dari
angka terkecil hingga angka terbesar.
Note: outputnya adalah list biasa, bukan list multi dimensi (list dalam list)
data = []
angka_ganjil = [13, 3, 5, 1, 7, 11, 15, 9]
angka_genap = [4, 2, 6, 8, 12, 14, 10]'''
#jawab
data = []  
angka_ganjil = [13, 3, 5, 1, 7, 11, 15, 9] 
angka_genap = [4, 2, 6, 8, 12, 14, 10] 
data.extend(angka_genap+angka_ganjil) 
data.sort() 
print(data[::3]) 

print("\n") 

'''Soal 2
Mang Ucup sang owner niagara fruit memiliki segudang buah yang sangat banyak. Ada
apel, strawberry, buah naga, anggur, dan pisang. Karena banyak banget, dia pengen
ngejadiin dalam satu list buah.
List Buah :
buah = ["apel", "strawberry", "buah naga", "alpukat", "anggur", "pisang"]
Dia iseng ingin mencampur apel dengan pisang, strawberry dengan anggur, kemudian
buah naga dengan alpukat. Keisengannya berlanjut, dia ingin nama buahnya disebutkan
dari belakang. Bantu mang ucup untuk mewujudkan keisengannya
Output :
["lepa ngasip", "yrrebwarts ruggna", "agan haub takupla"]'''
#jawab
buah = ["apel", "strawberry", "buah naga", "alpukat", "anggur", "pisang"] 
buahbaru= [
    buah[0][::-1]+" "+buah[5][::-1],
    buah[1][::-1]+" "+buah[4][::-1],
    buah[2][::-1]+" "+buah[3][::-1]]

print(buahbaru)
print("\n")

'''Soal 3
Mang Fathan memiliki toko buah dan ingin menghitung keuntungan penjualan dari
berbagai jenis buah. Berikut adalah daftar harga dan jumlah buah yang terjual dalam satu
minggu:
harga_buah = [10000, 15000, 20000] #Harga dari : [Pisang, Apel, Jambu]
jumlah_terjual = [10, 5, 7] #Jumlah Penjualan : [Pisang, Apel, Jambu]
• Buatlah variabel total_pendapatan yang berisi hasil perhitungan total pendapatan
Andi dari penjualan semua buah dalam seminggu.
• Buatlah list baru yang berisi jumlah keuntungan Andi dari setiap jenis buah
(keuntungan per buah didapat dari harga buah dikali jumlah terjual).
• Cetak list pendapatan dari setiap buah yang terjual
• Cetak semua total pendapatan Mang Fathan'''

data_buah = {
    "Pisang": {"harga": 10000, "jumlah_terjual": 10},
    "Apel": {"harga": 15000, "jumlah_terjual": 5},
    "Jambu": {"harga": 20000, "jumlah_terjual": 7}
}

keuntungan_per_buah = [
    data_buah["Pisang"]["harga"] * data_buah["Pisang"]["jumlah_terjual"],
    data_buah["Apel"]["harga"] * data_buah["Apel"]["jumlah_terjual"],
    data_buah["Jambu"]["harga"] * data_buah["Jambu"]["jumlah_terjual"]
]

total_pendapatan = keuntungan_per_buah[0] + keuntungan_per_buah[1] + keuntungan_per_buah[2]

print("Keuntungan per buah:", keuntungan_per_buah)

kp = keuntungan_per_buah[0]
ka = keuntungan_per_buah[1]
kj = keuntungan_per_buah[2]

print("Keuntungan Pisang:", kp)
print("Keuntungan Apel:", ka)
print("Keuntungan Jambu:", kj)
print("Total pendapatan Mang Fathan:", total_pendapatan)
