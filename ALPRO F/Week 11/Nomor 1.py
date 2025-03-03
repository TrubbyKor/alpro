def hapus_baris(tes):
    with open(tes, 'r') as file:
        teks = file.read()

    tanpa_baris = teks.replace('\n', ' ')
    return tanpa_baris

def simpan_teks(teks, nama_berkas_output):
    with open(nama_berkas_output, 'w') as file:
        file.write(teks)

tes = 'D:/ALPRO F/Week 11/Tes_Tugas.txt'
teks_konversi = hapus_baris(tes)
print(teks_konversi)

output_file = 'D:/ALPRO F/Week 11/Penyimpanan_Tes' 
simpan_teks(teks_konversi, output_file)

print('Hasil telah disimpan ke', output_file)