# 1. Buatlah program anda pada praktikum minggu-minggu sebelumnya agar dapat menangani kesalahan dari masukkan pengguna!

def factorial(n):
    hasil = ""
    faktor = 1
    for i in range(n, 0, -1):
        faktor *= i
        hasil += str(i) + (" x " if i > 1 else "")
    print("Hasil dari faktorial",n, "adalah", hasil, "=",faktor)

while True:
    try:
        input_str = input("Masukkan bilangan bulat positif: ")
        
        n = int(input_str)
        if n < 0:
            raise ValueError("Input tidak boleh negatif!")
        
        factorial(n)
        
    except ValueError as e:
        if str(e) == "Input tidak boleh negatif!":
            print("Error:", str(e))
        else :
            print ("Masukkan angka, bukan huruf!")
            break
    
