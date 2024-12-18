import time

input("Tekan Enter untuk memulai stopwatch...")
start_time = time.time()

input("Tekan Enter lagi untuk menghentikan stopwatch...")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Waktu yang berlalu: {elapsed_time:.2f} detik.")
