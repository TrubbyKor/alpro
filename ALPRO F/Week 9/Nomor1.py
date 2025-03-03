# Buatlah fungsi untuk mencari nilai faktorial dari suatu angka. 
# Contoh dimasukkan 5, output : 5 x 4 x 3 x 2 x 1 = 120

def factorial(n):
    hasil = ""
    faktor = 1

    for i in range(n, 0, -1):
        faktor *= i
        hasil += str(i) + (" x " if i > 1 else "")
    
    print("hasil dari faktorial",n,"adalah",hasil, "=", faktor)
    
n = int(input("Masukkan Faktorial yang akan di hitung :"))
factorial(n)

