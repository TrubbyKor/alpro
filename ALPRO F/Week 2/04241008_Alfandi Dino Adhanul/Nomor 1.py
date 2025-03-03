# Buatlah program yang menerima input berupa tahun. 
Tahun = int(input("Masukkan Tahun :"))

# Program harus memeriksa apakah tahun tersebut 
# merupakan tahun kabisat atau bukan. Sebuah tahun kabisat dapat ditentukan dengan aturan sebagai berikut:
# Tahun tersebut habis dibagi 4, tetapi tidak habis dibagi 100, atau 
# Tahun tersebut habis dibagi 400

if (Tahun % 4 == 0 and Tahun % 100 != 0) or (Tahun % 400 ==0):
    print(f"Tahun {Tahun} Merupakan Tahun Kabisat") 
else :
    print(f"Tahun {Tahun} Bukan Tahun Kabisat")