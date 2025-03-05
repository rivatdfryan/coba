alas = int(input("Alas\t: "))
tinggi = int(input("Tinggi\t: "))
luas = (alas/2)*tinggi

print("luas segitiga tersebut adalah\t: ",luas)
# if luas%2==1 :
#     print("ganjil")
# elif luas%2==0 : 
#     print("genap")
# else :
#     print("tidak")

print("Ganjil",luas%2==1)
print("Genap",luas%2==0)