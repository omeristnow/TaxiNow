import os
import sistem
import time
print ("""4 Konum Üzerinde Yapılan Seferler
Sefer saatleri Saati 15,30,45 ve 00 da
Eğer 4 kişilik araç dolarsa hemen gidilebilir
""")

print ("""Konum Krokisi
Konum1 --------------------------------------------------------- Konum2
       *
        *
         *
          *
           *
            *
             *
              * *********************************************Konum 4
              Konum 3
""")

print ("""Ücretlendirme
Konum1 - Konum2  = 100 TL
Konum1 - Konum3 = 200 TL
Konum3 - Konum4 = 300
Konum2 - Konum4 = 80
""")
bulundugunuzkonum = input ("Bulunduğunuz Konum")
gideceginizkonum = input ("Gideceğiniz konum")
dosya_konum = "k"+bulundugunuzkonum+"-"+"k"+gideceginizkonum+".txt"
gidissayisi = open (dosya_konum,"r+")
aktifkisi = gidissayisi.readline()
aktifkisi_ekle = int(aktifkisi)+1
gidissayisi.close()
dosya_verigir = open(dosya_konum,"w")
dosya_verigir.write(str(aktifkisi_ekle))
dosya_verigir.close()
sistemrestarsayisi = 0
while True :
    print ("\n"*50)
    dosya_verikontrol= open(dosya_konum,"r+")
    aktif_veri = int(dosya_verikontrol.readline())
    sistemrestarsayisi = sistemrestarsayisi +1
    dosya_verikontrol.close()
    if sistemrestarsayisi % 100 == 0 :
        tercih = input("Çıkış yapmak ister misiniz Evet [E] yada Hayır [H]")
        if tercih == "E" or tercih == "e":
            aktif_cikis = aktif_veri - 1
            cikis = open(dosya_konum , "w")
            cikis.write(str(aktif_cikis))
            cikis.close()
            exit()
        else :
            pass
    print ("Sistem Aktif Olarak {}. Kere Network'u test ediyor".format(sistemrestarsayisi))
    if bulundugunuzkonum == "1" and gideceginizkonum == "2":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (100/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)

    if bulundugunuzkonum == "2" and gideceginizkonum == "1":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (100/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)

    if bulundugunuzkonum == "1" and gideceginizkonum == "3":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (200/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)
    if bulundugunuzkonum == "3" and gideceginizkonum == "1":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (200/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)
    if bulundugunuzkonum == "3" and gideceginizkonum == "4":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (300/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)
    if bulundugunuzkonum == "4" and gideceginizkonum == "3":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (300/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)
    if bulundugunuzkonum == "2" and gideceginizkonum == "4":
        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (80/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)
    if bulundugunuzkonum == "4" and gideceginizkonum == "2":

        print ("Sizle beraber aynı taxi yi bekleyen {} kullanıcı var".format(aktif_veri))
        ucret = float (80/aktif_veri)
        print ("Şu an ödeyeceğiniz ücret : {}".format(ucret))
        time.sleep(6)

    else :
        pass
