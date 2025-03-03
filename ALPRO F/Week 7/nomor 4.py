while True:
    kalimat = input("Masukkan kalimat aritmatika: ")

    if kalimat.lower() == "selesai":
        print("--PROGRAM SELESAI--")
        break

    kata = kalimat.split()

    angka1 = None
    angka2 = None
    for katainp in kata:
        if katainp.lstrip('-').isdigit(): 
            if angka1 is None:
                angka1 = int(katainp)
            elif angka2 is None:
                angka2 = int(katainp)
                break

    if angka1 is None or angka2 is None:
        print("Input tidak valid. Masukkan dua angka.")
        continue
    if "tambah" in kalimat or "ditambah" in kalimat or "ditambahkan" in kalimat:
        hasil = angka1 + angka2
    elif "kurang" in kalimat or "dikurang" in kalimat or "dikurangkan" in kalimat or "dikurangi" in kalimat:
        hasil = angka1 - angka2
    elif "kali" in kalimat or "dikali" in kalimat or "dikalikan" in kalimat:
        hasil = angka1 * angka2
    elif "bagi" in kalimat or "dibagi" in kalimat:
        if angka2 == 0:
            print("hasil tak terhingga.")
            continue
        hasil = angka1 / angka2
    else:
        print("Operasi tidak dikenali.")
        continue
    print("Hasil:", hasil)
    print ("ketik selesai jika ingin berhenti")
