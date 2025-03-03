# # Buatlah program untuk menghitung pajak penghasilan seseorang berdasarkan aturan pajak sebagai berikut:
# •	Jika penghasilan <= 50 juta, pajak 5%.
# •	Jika penghasilan > 50 juta dan <= 250 juta, pajak 15%.
# •	Jika penghasilan > 250 juta dan <= 500 juta, pajak 25%.
# •	Jika penghasilan > 500 juta, pajak 30%.

# Program harus menerima input berupa jumlah penghasilan, dan mengeluarkan output berupa pajak yang harus dibayar.
penghasilan = int(input("Masukkan Jumlah Penghasilan :"))

if (penghasilan <= 50000000) :
    pajak = penghasilan * 0.05
elif (penghasilan > 50000000 and penghasilan <= 250000000) :
    pajak = penghasilan * 0.15
elif (penghasilan > 250000000 and penghasilan <= 500000000) :
    pajak = penghasilan * 0.25
else :
    pajak = penghasilan * 0.3
     
print(f"Pajak yang harus dibayar: Rp {pajak:,.2f}")