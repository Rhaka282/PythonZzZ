def kerucut():
    tinggi= int(input('masukan nilai sisi\t: '))
    jarijari= int(input('masukan nilai sisi\t: '))
    
    phi = 22/7

    volume= lambda phi , tinggi , jarijari:  phi * jarijari * jarijari * tinggi

    print('sisi kerucut\t\t:',volume(phi,jarijari,tinggi), ' cm2')

kerucut()
kerucut()
kerucut()