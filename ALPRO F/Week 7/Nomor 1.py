kalimat = input("Masukkan kalimat: ")
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print("Kalimat terbalik:", kalimat_terbalik)

vokal = "aAeEiIoOuU"
jumlah = 0

for huruf in kalimat:
    if huruf in vokal:
        jumlah += 1

print("Jumlah huruf vokal:", jumlah)
