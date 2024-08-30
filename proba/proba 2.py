#formirati ocenu na osnovu osvojenih poena

p=int(input('Unesite osvojeni broj poena '))

if p>90:
    print('Dobili ste 10')
elif p>80:
    print('Dobili ste 9')
elif p>70:
    print('Dobili ste 8')
elif p>60:
    print('Dobili ste 7')
elif p>50:
    print('Dobili ste 6')
else:
   print('Pali ste na ispitu')

