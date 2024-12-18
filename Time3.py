import time

detik = int(input("Masukkan hitungan mundur (detik): "))

for i in range(detik, 0, -1):
    print(f"{i} detik tersisa...")
    time.sleep(1)  

print("Waktu selesai!")
