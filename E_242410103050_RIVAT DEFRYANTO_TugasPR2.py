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
data = []  #menambahkan variabel data yang bertipe list dari soal 
angka_ganjil = [13, 3, 5, 1, 7, 11, 15, 9] # nilai list angka_ganjil dari soal
angka_genap = [4, 2, 6, 8, 12, 14, 10] # nilai list angka_genap dari soal
data.extend(angka_genap+angka_ganjil) # menggabungkan dan memasukkan nilai variabel list angka_ganjil dan angka_genap kedalam variabel data yang terdapat pada line 14.
data.sort() # mengurutkan nilai list dari variabel data dari yang terkecil hingga terbesar
print(data[::3]) #menampilkan output dari variabel data, juga dengan menambahkan interval atau pola(step) sebanyak 3 agar nilai yang telah diurutkan sebelumnyanditampilkan dengan selisih 3 angka, yakni 1,4,7,10,13

print("\n") # Hanya sekedar membuat newline untuk membuat jarak output soal berikutnya

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
buah = ["apel", "strawberry", "buah naga", "alpukat", "anggur", "pisang"] #membuat list dengan nama variabel buah sesusai dengan yang ada di soal
buah1=buah[5]+" "+buah[0] #membuat variabel baru (buah1), yang bernilai penggabungan dari index ke 5 variabel buah, yakni "pisang" dengan index ke 0 dari variabel buah yakni "apel". penambahan (" ") ditengah keduanya agar pisang dan apel memiliki spasi ketika digabungkan. sehingga isi dari variabel buah1 ini yakni "pisang apel"
buah2=buah[4]+" "+buah[1] #membuat variabel baru (buah2), yang bernilai penggabungan dari index ke 4 variabel buah, yakni "anggur" dengan index ke 1 dari variabel buah yakni "strawberry". sehingga isi dari variabel buah 2 ini yakni "anggur strawberry"
buah3=buah[3]+" "+buah[2] #membuat variabel baru (buah3), yang bernilai penggabungan dari index ke 3 variabel buah, yakni "alpukat" dengan index ke 2 dari variabel buah yakni "buah naga". sehingga isi dari variabel buah 2 ini yakni "alpukat buah naga"
#print([buah1,buah2,buah3]) # menampilkan output dari buah milik mang ucup yang belum dibalik tulisannya
print([buah1[::-1],buah2[::-1],buah3[::-1]]) # menampilkan buah milik mang ucup yang tulisannya disebutkan dari belakang atau menampilkan output dari list buah1, buah2, dan buah 3 yang digabung lalu dibalik urutan nilainya.

print("\n")

# buahbaru= [
#     buah[0][::-1]+" "+buah[5][::-1],
#     buah[1][::-1]+" "+buah[4][::-1],
#     buah[2][::-1]+" "+buah[3][::-1]]

# print(buahbaru)

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
nama_buah = ["Pisang", "Apel", "Jambu"]
harga_buah = [10000, 15000, 20000] #membuat variabel list harga_buah yang berisi harga penjualan buah sesusai dengan soal
jumlah_terjual = [10, 5, 7]  #membuat variabel jumlah_terjual ynag berisi jumlah penjualan buah sesuai dengan soal
tp= harga_buah[0]*jumlah_terjual[0] #membuat variabel baru(tp) untuk menampung nilai dari pendapatan buah pisang, dengan cara mengkalikan index ke 0 dari list harga_buah dengan index ke 0 dari list jumlah_terjual (pendapatan didapat dari harga buah dikali jumlah penjualan, 10.000 x 10)
ta= harga_buah[1]*jumlah_terjual[1] #membuat variabel baru(ta) untuk menampung nilai dari pendapatan buah apel, dengan cara mengkalikan index ke 1 dari list harga_buah dengan index ke 1 dari list jumlah_terjual (15.000 x 5)
tj= harga_buah[2]*jumlah_terjual[2] #membuat variabel baru(tj) untuk menampung nilai dari pendapatan buah jambu, dengan cara mengkalikan index ke 2 dari list harga_buah dengan index ke 2 dari list jumlah_terjual (20.000 x 7)
total_pendapatan = ta+tp+tj #membuat variabel total_pendapatan yang berisi hasil perhitungan total pendapatan semua buah andi, total pendapatan didapat dari penjumlahan nilai pendapatan semua buah yang  telah ditampung pada variabel sebelumnya.
lispendapatan = [tp,ta,tj] #membuat variabel baru yang berisi list pendapatan dari setiap buah yang terjual.
print(lispendapatan) # menampilkan output(mencetak) list pendapatan dari setiap buah yang terjual, dengan urutan pisang,apel,jambu

print ("=====TOTAL PENDAPATAN MANG FATHAN=======") #sekedar menghias
print ("Pendapatan",nama_buah[0],"\t:",tp) #menampilkan output dari total penjualan pisang mang fathan
print ("Pendapatan",nama_buah[1],"\t:",ta) #menampilkan output dari total penjualan apel mang fathan
print ("Pendapatan",nama_buah[2],"\t:",tj) #menampilkan output dari total penjualan jambu mang fathan
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #sekedar menghias
print ("TOTAL PENDAPATAN\t:",total_pendapatan) #menampilkan output(mencetak) total semua pendapatan mang fathan. total seluruhnya telah ditampung sebelumnya pada variabel total_pendapatan, sehingga pada bagian ini tinggal memanggil saja nilai dari variabel tersebut
print ("========================================")#sekedar menghias