try:
    kalimat = input("Masukkan kalimat: ")
    if not kalimat:
        raise ValueError("Kalimat tidak boleh kosong.")

    # Membalik kalimat
    kalimat_terbalik = ""
    for huruf in kalimat:
        kalimat_terbalik = huruf + kalimat_terbalik

    print("Kalimat terbalik:", kalimat_terbalik)

    # Menghitung huruf vokal
    vokal = "aAeEiIoOuU"
    jumlah = 0
    for huruf in kalimat:
        if huruf in vokal:
            jumlah += 1

    print("Jumlah huruf vokal:", jumlah)

except ValueError as e:
    print(e)
