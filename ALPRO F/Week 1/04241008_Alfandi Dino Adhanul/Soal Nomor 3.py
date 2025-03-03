# Buatlah program untuk menghitung gaji pegawai dalam satu minggu dimana
# masukkan pengguna berupa upah pegawai per jam dengan asumsi satu hari kerja
# adalah 8 jam!

Gaji_Pegawai = int(input("Masukkan upah pegawai per jam :"))

#Upah pegawai perjam di kali dengan 8 jam yang di mana satu hari kerja ada;ah 8 jam
#kemudian di kali lagi dengan 7 hari atau satu minggu
gaji = (Gaji_Pegawai * 8) * 7
print("Gaji pegawai", Gaji_Pegawai, "per jam dalam satu minggu adalah", gaji, "Rupiah")