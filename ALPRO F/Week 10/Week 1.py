import math

try:
    tinggi = float(input("Masukkan tinggi: "))
    jari_jari = float(input("Masukkan jari-jari: "))

    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

    print(f"Luas Permukaan Tabung: {luas_permukaan:.4f}")
    
except ValueError:
    print("Input harus berupa angka. Silakan masukkan nilai yang benar.")
