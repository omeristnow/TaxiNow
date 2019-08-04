import os
def olustur ():
    dosya_konum = "sistemaktif.txt"
    a = open(dosya_konum,"w")
    a.write("Taksi Sistemi aktif...")
    a.close()
    dosya_konum = "k"+"1"+"-"+"k"+"2"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"1"+"-"+"k"+"3"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"3"+"-"+"k"+"4"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"2"+"-"+"k"+"4"+".txt"
    a.close()
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"2"+"-"+"k"+"1"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"3"+"-"+"k"+"1"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"4"+"-"+"k"+"3"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
    dosya_konum = "k"+"4"+"-"+"k"+"2"+".txt"
    a = open(dosya_konum,"w")
    a.write("0")
    a.close()
def kaldir ():
    dosya_konum = "sistemaktif.txt"
    os.remove(dosya_konum)
    dosya_konum = "k"+"1"+"-"+"k"+"2"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"1"+"-"+"k"+"3"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"3"+"-"+"k"+"4"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"2"+"-"+"k"+"4"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"2"+"-"+"k"+"1"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"3"+"-"+"k"+"1"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"4"+"-"+"k"+"3"+".txt"
    os.remove (dosya_konum)
    dosya_konum = "k"+"4"+"-"+"k"+"2"+".txt"
    os.remove (dosya_konum)

if os.path.exists("sistemaktif.txt") == True :
    pass
else :
    olustur()
