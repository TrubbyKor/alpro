try:
    n = int(input("Masukkan nilai: "))
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(".", end="")
        print(i)
except ValueError:
    print("Input harus berupa angka bulat.")
