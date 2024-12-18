def prisma():
    alas= int(input('masukan nilai sisi\t: '))
    La= int(input('masukan nilai sisi\t: '))
    Tinggi= int(input('masukan nilai sisi\t: '))

    volume = lambda La,Tinggi: La * Tinggi

    print('sisi prisma\t\t:',volume(La,Tinggi),' cm2')

prisma()
prisma()
prisma()