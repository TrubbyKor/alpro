# Buatlah program untuk mencari cicilan rumah per tahun dengan diketahui harga rumah asal, 
# harga rumah yang dijual ke klien, dan lama waktu cicilan dengan skema 20, 15, 10, dan 5 tahun.


harga_asal = float(input("Masukkan harga rumah asal: "))
harga_jual = float(input("Masukkan harga rumah yang dijual ke klien: "))

pinjaman = harga_jual - harga_asal
for lama_cicilan in range (20, 4, -5):
    cicilan_per_tahun = pinjaman / lama_cicilan
    print(f"Cicilan per tahun untuk {lama_cicilan} tahun: {cicilan_per_tahun:.2f}")
