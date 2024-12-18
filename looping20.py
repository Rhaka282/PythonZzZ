print('='*60)
print('\t\tperkalian\t\t')
print('='*60)


z = int(input("masukan jumlah perkalian: "))

print("output:")
print("    *", end='')
for x in range(1, z + 1):
    print(f"{x:5}", end="")
print()

for x in range(1,z + 1):
    print(f"{x:5}", end="")
    for y in range(1, z + 1):
        print(f"{x * y:5}", end="")
    print()          