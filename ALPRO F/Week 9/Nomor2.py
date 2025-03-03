# Buatlah fungsi yang merepresentasikan fungsi matematika berikut : y=6x2+3x+2 
# Yang memberikan keluaran berupa nilai y dimana x adalah bilangan bulat antara -10 sampai 10.

def hitung(x):
    return 6*x**2 + 3*x + 2

for x in range(-10, 11):
    y = hitung(x)
    print("x =", x, "y =",y)