print("Program untuk mencari nilai faktorial")

try:
    Angka = int(input("Masukkan angka: "))
    
    if Angka < 0:
        print("Faktorial hanya bisa dihitung untuk bilangan non-negatif.")
    else:
        fak = 1
        x = Angka
        Hasil = ""

        while x > 0:
            fak *= x
            Hasil += str(x) + (" x " if x > 1 else "")
            x -= 1
        
        print(Angka,"! = ",Hasil, "=", fak)

except ValueError:
    print("Input harus berupa angka bulat.")
