def limas():
    alas= int(input('masukan nilai sisi\t: '))
    sisi= int(input('masukan nilai sisi\t: '))
    tegak= int(input('masukan nilai sisi\t: '))

    luas = lambda alas,sisi,tegak: alas * sisi * tegak

    print('sisi limas\t\t:',luas(alas,sisi,tegak),' cm2')

limas()
limas()
limas()