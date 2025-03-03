def kata(nama_berkas):
    with open(nama_berkas, 'r') as file:
        teks = file.read()
    kata_kata = teks.split()

    daftar_kata = [(kata, idx + 1) for idx, kata in enumerate(kata_kata)]
    return daftar_kata

def simpan(daftar_kata, nama_berkas_output):
    with open(nama_berkas_output, 'w') as file:
        for kata, posisi in daftar_kata:
            file.write('{}: {}\n'.format(kata, posisi))

nama_berkas_input = 'D:/ALPRO F/Week 11/Tes_Tugas.txt'
daftar_kata = kata(nama_berkas_input)

for kata, posisi in daftar_kata:
    print(kata,':', posisi)

berkas_output = 'D:/ALPRO F/Week 11/Daftar_Kata'
simpan(daftar_kata, berkas_output)
print('Hasil telah disimpan ke', berkas_output)