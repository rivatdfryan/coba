tgl = int(input("Masukkan tanggal lahir anda\t:"))
bln = int(input("Masukkan bulan lahir anda\t:"))

if (1<=tgl<=19) & (bln==1) | (22>=tgl<=31) & (bln==12) :
    print("Zodiak anda adalah Capricorn") 
elif (20<=tgl<=29) & (bln==1) | (1<=tgl<=18) & (bln==2) :
    print("Zodiak anda adalah Aquarius") 
elif (19<=tgl<=31) & (bln==2) | (1<=tgl<=20) & (bln==3) :
    print("Zodiak anda adalah Pisces") 
elif (21<=tgl<=31) & (bln==3) | (1<=tgl<=19) & (bln==4) :
    print("Zodiak anda adalah Aries") 
elif (20<=tgl<=31) & (bln==4) | (1<=tgl<=20) & (bln==5) :
    print("Zodiak anda adalah Taurus") 
elif (21<=tgl<=31) & (bln==5) | (1<=tgl<=20) & (bln==6) :
    print("Zodiak anda adalah Gemini") 
elif (21<=tgl<=31) & (bln==6) | (1<=tgl<=22) & (bln==7) :
    print("Zodiak anda adalah Cancer") 
elif (23<=tgl<=31) & (bln==7) | (1<=tgl<=22) & (bln==8) :
    print("Zodiak anda adalah Leo") 
elif (23<=tgl<=31) & (bln==8) | (1<=tgl<=22) & (bln==9) :
    print("Zodiak anda adalah Virgo") 
elif (23<=tgl<=31) & (bln==9) | (1<=tgl<=22) & (bln==10) :
    print("Zodiak anda adalah Libra") 
elif (23<=tgl<=31) & (bln==10) | (1<=tgl<=21) & (bln==11) :
    print("Zodiak anda adalah Scorpio") 
elif (22<=tgl<=31) & (bln==11) | (1<=tgl<=21) & (bln==12) :
    print("Zodiak anda adalah Sagittarius") 
else :
    print("tidak bisa")
