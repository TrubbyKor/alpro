try:
    Tahun = int(input("Masukkan Tahun: "))
    if (Tahun % 4 == 0 and Tahun % 100 != 0) or (Tahun % 400 == 0):
        print("Tahun",Tahun, "Merupakan Tahun Kabisat")
    else:
        print("Tahun",Tahun, "Bukan Tahun Kabisat")
except ValueError:
    print("Error: Harap masukkan angka untuk tahun, bukan huruf atau karakter lain!")
