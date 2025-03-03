baris1 = int(input("Masukkan jumlah baris untuk matriks pertama: "))
kolom1 = int(input("Masukkan jumlah kolom untuk matriks pertama: "))

baris2 = int(input("Masukkan jumlah baris untuk matriks kedua: "))
kolom2 = int(input("Masukkan jumlah kolom untuk matriks kedua: "))

if kolom1 != baris2:
    print("Perkalian matriks tidak bisa dilakukan. Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
else:
    print("\nMasukkan elemen matriks pertama:")
    matriks1 = []
    for i in range(baris1):
        baris = []
        for j in range(kolom1):
            elemen = int(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            baris.append(elemen)
        matriks1.append(baris)

    print("\nMasukkan elemen matriks kedua:")
    matriks2 = []
    for i in range(baris2):
        baris = []
        for j in range(kolom2):
            elemen = int(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            baris.append(elemen)
        matriks2.append(baris)

    hasil = []
    for i in range(baris1):
        baris = []
        for j in range(kolom2):
            baris.append(0)
        hasil.append(baris)

    for i in range(baris1):
        for j in range(kolom2):
            for k in range(kolom1):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    print("\nHasil perkalian matriks:")
    for baris in hasil:
        for elemen in baris:
            print(elemen, end=" ")
        print()
