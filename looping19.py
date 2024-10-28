jumlah = int(input("Masukan jumlah nilainya \t: "))

total= 0
for a in range (jumlah):
    nilai1 = int(input("Masukan Nilainya \t\t: "))
    total += nilai1

rata_rata = total / jumlah
print("Jumlah Nilai adalah \t\t:",total)
print("Rata - Rata Nilainya adalah \t:",rata_rata)