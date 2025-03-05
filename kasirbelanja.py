import os

# Daftar belanja
daftar_belanja = []

def tambah_item():
    nama = input("Masukkan nama item: ")
    jumlah = int(input("Masukkan jumlah: "))
    harga = float(input("Masukkan harga per unit: "))
    total_harga = jumlah * harga
    item = {
        "nama": nama,
        "jumlah": jumlah,
        "total_harga": total_harga
    }
    daftar_belanja.append(item)
    print(f"Item '{nama}' telah ditambahkan ke daftar belanja.\n")

def lihat_daftar_belanja():
    if not daftar_belanja:
        print("Daftar belanja kosong.\n")
        return
    print("Daftar Belanja Anda:")
    print("----------------------------------------")
    print("No | Nama Item   | Jumlah | Harga Total")
    for i, item in enumerate(daftar_belanja, start=1):
        print(f"{i}  | {item['nama']:<10} | {item['jumlah']:<6} | Rp{item['total_harga']:.2f}")
    total = sum(item['total_harga'] for item in daftar_belanja)
    print("----------------------------------------")
    print(f"Total: Rp{total:.2f}\n")

def hapus_item():
    lihat_daftar_belanja()
    if not daftar_belanja:
        return
    try:
        nomor = int(input("Masukkan nomor item yang ingin dihapus: "))
        if 1 <= nomor <= len(daftar_belanja):
            item = daftar_belanja.pop(nomor - 1)
            print(f"Item '{item['nama']}' telah dihapus dari daftar belanja.\n")
        else:
            print("Nomor item tidak valid.\n")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.\n")

def simpan_ke_file():
    filename = "daftar_belanja.txt"
    with open(filename, "w") as file:
        for item in daftar_belanja:
            file.write(f"{item['nama']},{item['jumlah']},{item['total_harga']}\n")
    print(f"Daftar belanja telah disimpan ke file '{filename}'.\n")

def muat_dari_file():
    filename = "daftar_belanja.txt"
    if not os.path.exists(filename):
        print(f"File '{filename}' tidak ditemukan.\n")
        return
    with open(filename, "r") as file:
        daftar_belanja.clear()
        for line in file:
            nama, jumlah, total_harga = line.strip().split(',')
            daftar_belanja.append({
                "nama": nama,
                "jumlah": int(jumlah),
                "total_harga": float(total_harga)
            })
    print(f"Daftar belanja telah dimuat dari file '{filename}'.\n")

def menu_utama():
    while True:
        print("Selamat Datang di Aplikasi Manajemen Daftar Belanja")
        print("Pilih opsi berikut:")
        print("1. Tambah Item")
        print("2. Lihat Daftar Belanja")
        print("3. Hapus Item")
        print("4. Simpan Daftar ke File")
        print("5. Muat Daftar dari File")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            tambah_item()
        elif pilihan == '2':
            lihat_daftar_belanja()
        elif pilihan == '3':
            hapus_item()
        elif pilihan == '4':
            simpan_ke_file()
        elif pilihan == '5':
            muat_dari_file()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    menu_utama()
