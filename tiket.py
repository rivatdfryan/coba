sby = 10000
bl = 20000
lmp = 30000
org = input("Nama pembeli : ")
hp = input("Nomor Handphone : ")
print("\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("| Kodejurusan\t|","Nama kota\t|","Harga","|")
print("| SBY\t\t|","Surabaya\t|",sby,"|")
print("| BL\t\t|","Bali\t\t|",bl,"|")
print("| LMP\t\t|","Lampung\t|",lmp,"|")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")

jrsn = input("Masukkan kode jurusan yang anda mau\t: ").upper()
tkt = int(input("Jumlah tiket\t\t\t\t: "))

total=()

if jrsn == "SBY" :
    total = (tkt*sby)
    print ("Harga tiket anda\t\t\t:", total)
    
elif jrsn == "BL" :
    total = (tkt*bl)
    print ("Harga tiket anda\t\t\t:", total)
    
elif jrsn == "LMP" :
    total = (tkt*lmp)
    print ("Harga tiket anda\t\t\t:", total)
    
else :
    print("Kode jurusan salah") 
    
# diskon = int()

if tkt>=3 :
    diskon = int(total*0.1)
    print("Anda mendapat diskon 10%")
else :
    print("Tidak mendapat diskon")
  
akhir= (total-diskon)
print("Harga tiket akhir\t\t\t:", akhir)
print("\n")

pilih = input("Pembayaran cash / tf ? : ").upper()
if pilih == "CASH" :
    akhir= (int(total)-diskon)
    print("\n")
    print("berikut struk pembayaran anda :")
    print ("============Ngawi  Bus==================")
    print ("Nama pembeli\t\t:",org)
    print ("Nomor handphone\t\t:",hp)
    print ("jurusan\t\t\t:",jrsn)
    print ("jumlah tiket\t\t:",tkt)
    print ("jumlah pembayaran\t:",akhir)
    print ("========================================")
    print ("note :")
    print ("silahkan melakukan pembayaran di loket terdekat")


elif pilih == "TF" :
    print("Silahkan melakukan pembayaran")
    bayar = int( input("Masukkan saldo anda :"))
    kris = int(bayar-akhir)
    if bayar >= akhir :
        print("Pembayaran berhasil")
        print("Saldo anda :",bayar)
        print("Kembalian :",kris)
        print("\n")
        print("Berikut bukti pembayaran anda :")
        print ("============Ngawi  Bus=================")
        print ("Nama pembeli\t\t:",org)
        print ("Nomor handphone\t\t:",hp)
        print ("jurusan\t\t\t:",jrsn)
        print ("jumlah tiket\t\t:",tkt)
        print ("jumlah pembayaran\t:",int(akhir))
        print ("jenis pembayaran\t: Transfer", )
        print ("status pembayaran \t: Lunas", )
        print ("=======================================")
    else :
        print ("maaf saldo anda kurang")
else :
    print ("pilih yang bener")