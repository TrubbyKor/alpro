# Buatlah program untuk mencari nilai faktorial. Misal dimasukkan angka 4 maka
# hasilnya adalah 24 (4! = 4 x 3 x 2 x 1 = 24). Keluaran harus mencetak penjabaran
# dari faktorial tersebut. Contoh :
# Input : 4
# # Output : 4! = 4 x 3 x 2 x 1 = 24

print ("untuk mencari nilai faktorial")


Angka = int(input("Masukkan angka: "))
fak = 1
x = Angka
Hasil = ""

while (x > 0) :
    fak *= x
    Hasil += str(x) + (" x " if x > 1 else "")
    x -=1
print(Angka,"! =", Hasil, "=", fak)