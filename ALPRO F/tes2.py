# Fungsi untuk menampilkan matriks
def tampilkan_matriks(matriks):
    for baris in matriks:
        print(" ".join(str(x) for x in baris))

# Program utama
def main():
    # Input ukuran matriks dari pengguna
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    
    # Membuat matriks dengan nilai awal 0
    matriks = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    # Menampilkan menu
    while True:
        print("\nMenu:")
        print("1. Tampilkan Matriks")
        print("2. Ubah Nilai Matriks")
        print("3. Keluar")
        
        # Pilihan menu
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            # Menampilkan matriks
            print("\nMatriks saat ini:")
            tampilkan_matriks(matriks)
        
        elif pilihan == "2":
            # Ubah nilai matriks
            try:
                b = int(input("Masukkan indeks baris (dimulai dari 0): "))
                k = int(input("Masukkan indeks kolom (dimulai dari 0): "))
                nilai_baru = int(input("Masukkan nilai baru: "))
                
                # Memastikan indeks berada dalam batas matriks
                if 0 <= b < baris and 0 <= k < kolom:
                    matriks[b][k] = nilai_baru
                    print(f"Nilai di baris {b}, kolom {k} berhasil diubah menjadi {nilai_baru}.")
                else:
                    print("Indeks baris atau kolom di luar batas!")
            
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
        
        elif pilihan == "3":
            # Keluar dari program
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, silakan pilih 1, 2, atau 3.")

# Menjalankan program
main()
