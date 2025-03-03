#Buatlah program untuk mencari luas permukaan tabung dimana jari-jari dan tinggi berasal dari masukkan pengguna
import math
tinggi = float(input("masukkan tinggi :"))
jari_jari = float(input("masukkan jari jari :"))

#masukkan rumus  2 π r (r + t)
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
# print("Luas Permukaan Tabung :", luas_permukaan:.2f)
print(f"Luas Permukaan Tabung : {luas_permukaan: .4f}")