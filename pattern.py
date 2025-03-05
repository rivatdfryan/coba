print(f"Nama\t\t:Rivat Defryanto\nNIM\t\t:242410103050\nMata kuliah\t:Algoritma dan Pemrograman 1(TM)\nKelas\t\t: E\nTugas\t\t:Perulangan segitiga\n\n")
for baris in range(1, 10):
    for kolom in range(9 - baris):
        print("  ", end="")
    for kolom in range(baris):
        print("* ", end="")
    for kolom in range(baris - 1):
        print("* ", end="")
    print()

# for baris in range(6, 0, -1):
#     for kolom in range(7-baris):
#         print("  ", end="") 
#     for kolom in range(baris):
#         print("* ", end="")
#     for kolom in range(baris - 1):
#         print("* ", end="")
#     print()
