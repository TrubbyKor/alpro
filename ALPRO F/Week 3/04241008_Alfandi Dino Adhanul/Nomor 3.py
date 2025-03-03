# Buatlah program untuk menghitung akar-akar persamaan kuadrat dengan rumus : 𝑫=𝒃𝟐−𝟒 ×𝒂×𝒄
import math
print("\033[33m .:: program untuk menghitung akar-akar persamaan kuadrat ::.")
a = float(input("\033[37m Masukkan a :"))
b = float(input("Masukkan b :"))
c = float(input("Masukkan c :"))
D = b**2 - 4 * a * c

# Jika D < 0, akar imajiner
if D < 0 :
    print("\033[37m akar imajiner")
elif D == 0 : 
    x = -b / (2 * a)
    print("\033[37m Akar-akarnya adalah kembar: x1 = x2 = ", (x))
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("\033[37m Akar-akarnya adalah: x1 = ", (x1), "dan x2 = ", (x2))
