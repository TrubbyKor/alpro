# Buatlah fungsi untuk mendeteksi apakah suatu angka yang dimasukkan merupakan bilangan prima atau bukan !
def prima(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

x = int(input("Masukkan angka: "))
if prima(x):
    print(x, "adalah bilangan prima.")
else:
    print(x, "bukan bilangan prima.")
