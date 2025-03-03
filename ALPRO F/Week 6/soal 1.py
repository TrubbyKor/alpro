print("Program Matriks")

baris = int(input("Masukkan jumlah baris matriks: "))
kolom = int(input("Masukkan jumlah kolom matriks: "))

matriks = {i: [0] * kolom for i in range(baris)}

while True:
    print("\nMenu:")
    print("1. Tampilkan Matriks")
    print("2. Ubah Nilai Matriks")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        print("Matriks:")
        for i in range(baris):
            for j in range(kolom):
                print(matriks[i][j], end=" ") 
            print() 
    
    elif pilihan == '2':
            b = int(input(f"Masukkan nomor baris (0 - {baris - 1}): "))
            k = int(input(f"Masukkan nomor kolom (0 - {kolom - 1}): "))

            nilai = int(input("Masukkan nilai baru: "))
            
            if 0 <= b < baris and 0 <= k < kolom:
                matriks[b][k] = nilai
                for i in range(baris):
                    for j in range(kolom):
                        print(matriks[i][j], end=" ")
                    print() 
            else:
                print("Baris atau kolom di luar jangkauan.")

    
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")