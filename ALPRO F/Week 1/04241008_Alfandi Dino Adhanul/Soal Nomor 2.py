#Buatlah program untuk mengkonversi suhu dari celcius ke fahrenheit !
celcius = float(input("Masukkan Suhu dalam \u00b0 celcius :"))

#masukkan rumus: °F = (9/5 x °C) + 32
Fahrenheit = ( 9 / 5 * celcius ) + 32
# print("suhu", celcius, "°C dalam fahrenheit adalah", Fahrenheit, "°F") 
print(f"suhu {celcius} °C dalam fahrenheit adalah {Fahrenheit} °F")