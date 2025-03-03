print("\033[37m .:: Program Penerjemah Protein ::.")

try:
    # Menerima input kodon dari pengguna
    Kodon = input("Masukkan Kodon: ").upper()
    
    # Menerjemahkan kodon ke nama protein
    if Kodon == 'AUG':
        print("Protein : Methionine")
    elif Kodon in ['UUU', 'UUC']:
        print("Protein : Phenylalanine")
    elif Kodon in ['UUA', 'UUG']:
        print("Protein : Leucine")
    elif Kodon in ['UCU', 'UCC', 'UCA', 'UCG']:
        print("Protein : Serine")
    elif Kodon in ['UAU', 'UAC']:
        print("Protein : Tyrosine")
    elif Kodon in ['UGU', 'UGC']:
        print("Protein : Cysteine")
    elif Kodon == 'UGG':
        print("Protein : Tryptophan")
    else:
        print("\033[31m Masukkan Kodon Yang Benar")
        
except Exception as e:
    print("\033[31m Terjadi kesalahan:", e)
