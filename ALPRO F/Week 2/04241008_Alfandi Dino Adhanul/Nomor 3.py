# Buatlah program yang menentukan nilai huruf dari seorang mahasiswa berdasarkan skala nilai 

# Program harus meminta input nilai numerik dan mengeluarkan output nilai huruf.
Nilai = float(input("Masukkan nilai mahasiswa :"))

# •	A: >= 85
# •	B: >= 70 dan < 85
# •	C: >= 55 dan < 70
# •	D: >= 40 dan < 55
# •	E: < 40
if (Nilai >= 85) :
    print ("A")
elif (Nilai >= 70 and Nilai < 85) :
    print ("B")
elif (Nilai >= 55 and Nilai < 70) :
    print ("C")
elif (Nilai >= 40 and Nilai < 55) :
    print ("D")
elif (Nilai < 40) :
    print ("E")