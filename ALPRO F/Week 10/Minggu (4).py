print("Program untuk mencetak bilangan ganjil dari N sampai dengan 1")

try:
    Batas = int(input("Masukkan bilangan bulat: "))
    while Batas >= 1:
        if Batas % 2 == 1:
            print(Batas, end=" ")
        Batas -= 1
except ValueError:
    print("Error: Masukkan bilangan bulat!")