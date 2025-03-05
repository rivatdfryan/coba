# for i in range (1,7) :
#     for j in range (i) :
#         print ("*", end=" ")
#     print (" ")
# for i in range (1,7) :
#     for j in range (i,6) :
#         print ("*", end=" ")
#     print (" ")

for baris in range (1,10) :
    for kolom in range (baris,9) :
        print (" ", end =" ")
    for kolom in range ,(baris,9) :
        print (" ", end =" ")
    for kolom in range (baris-1) :
        print ("*", end=" ")
    for kolom in range (baris) :
        print ("*", end=" ")
    print (" ")
for baris in range (1,10) :
    for kolom in range (baris+2) :
        print (" ", end =" ")
    for kolom in range (baris,9) :
        print ("*", end=" ")
    for kolom in range (baris+1,9) :
        print ("*", end=" ")
    for kolom in range (baris) :
        print (" ", end=" ")
    print (" ")
print("\n")

# BINGKDIAMOND
for y in range (16):  
    print("*",end=" ")
print()
for baris in range (1,8) :
    for kolom in range (baris,8) :
        print ("*", end =" ")
    for kolom in range (baris-1) :
        print (" ", end =" ")
    for kolom in range (baris+1) :
        print (" ", end=" ")
    for kolom in range (baris,8) :
        print ("*", end=" ")
    print (" ")
for baris in range (1,8) :
    for kolom in range (baris) :
        print ("*", end =" ")
    for kolom in range (baris,8) :
        print (" ", end=" ")
    for kolom in range (baris,8) :
        print (" ", end=" ")
    for kolom in range (baris) :
        print ("*", end=" ")
    print (" ")
for y in range (16):  
    print("*",end=" ")

