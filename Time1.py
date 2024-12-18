import time

start_time = time.time()

for i in range(1, 1000000):
    pass  

end_time = time.time()

durasi = end_time - start_time
print(f"Program dieksekusi selama {durasi:.4f} detik.")
