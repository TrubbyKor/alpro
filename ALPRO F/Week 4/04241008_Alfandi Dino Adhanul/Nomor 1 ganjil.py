# Buatlah program untuk mencetak bilangan ganjil dari N sampai dengan 1 dimana
# N adalah bilangan bulat masukkan pengguna. Sebagai contoh ketika pengguna
# memasukkan 10, maka komputer akan mencetak 9 7 5 3 1

print ("Program untuk mencetak bilangan ganjil dari N sampai dengan 1 ")

Batas=int(input("Masukkan bilangan bulat: "))
angka=1
while (Batas >= angka) : 
    if (Batas % 2 == 1) : 
        print (Batas, end= ",")
    Batas -=1
    