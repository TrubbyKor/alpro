n = int(input("Masukkan nilai: "))

for i in range(n, 0, -1):
    if i % 2 == 1:
        print('x' * i)
    else:
        print('-' * i)
