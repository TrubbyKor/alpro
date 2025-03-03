# Buatlah program penerjemah protein yang menerima masukkan berupa kodon dan memberikan keluaran berupa nama protein.
print(" \033[37m .:: Program Penerjemah Protein ::.")
Kodon = input("Masukkan Kodon : ")
if Kodon == 'AUG':
    print ("Protein : Methionine")
elif Kodon == 'UUU' and 'UUC':
    print ("Protein : Phenylalanine ")
elif Kodon == 'UUA' and 'UUG':
    print ("Protein : Leucine ")
elif Kodon == 'UCU' and 'UCC' and 'UCA' and 'UCG':
    print ("Protein : Serine")
elif Kodon == 'UAU' and 'UAC':
    print ("Protein : Tyrosine") 
elif Kodon == 'UGU' and 'UGC':
    print ("Protein : Cysteine")
elif Kodon == 'UGG':
    print ("Protein : Tryptophan")
else : 
    print ("\033[31m Masukan Kodon Yang Benar")                   