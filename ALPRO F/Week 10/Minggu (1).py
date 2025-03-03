try:
    Gaji_Pegawai = int(input("Masukkan upah pegawai per jam: "))
    gaji = (Gaji_Pegawai * 8) * 7
    print("Gaji pegawai", Gaji_Pegawai, "per jam dalam satu minggu adalah", gaji, "Rupiah")
except ValueError:
    print("Error: Harap masukkan angka untuk upah pegawai, bukan huruf atau karakter lain!")
