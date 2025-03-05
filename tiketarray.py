# sby = 10000
# bl = 20000
# lmp = 30000
kode = ["sby","bl","lmp"]
harga = [10000,20000,30000]
tujuan = ["Surabaya","Bali\t","Lampung"]
z=len(kode)
q = len(harga)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("| Kodejurusan\t |"," Nama kota\t |","Harga","|")
# print("| Kodejurusan\t |"," Nama kota\t |","Harga","|")
print("| Kodejurusan\t |"," Nama kota\t |","Harga","|")
for x in range (z) :
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|",kode[x],"\t\t","|",tujuan[x],"\t","|",harga[x],"|")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")