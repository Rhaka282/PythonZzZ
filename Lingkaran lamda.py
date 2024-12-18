def lingkaran():
    jarijari= int(input('masukan nilai sisi\t: '))

    phi=22/7

    luas = lambda phi, jarijari: phi * jarijari * jarijari
  
    print('sisi lingkaran\t\t:',luas(phi,jarijari), ' cm2')

lingkaran()
lingkaran()
lingkaran()