recnik={}

with open('proba.txt','r',encoding='utf-8') as fajl:
    for line in fajl:
        nadimak, pol,*imena=line.split()
        imena=" ,".join(imena)
        if nadimak not in recnik:
            recnik[nadimak]=[pol, imena]
        else:
            recnik[nadimak][1]+=' ,'+imena
            if pol!=recnik[nadimak][0]:
                recnik[nadimak][0]='2'

with open('newfile.txt','w', encoding='utf-8') as upisni_fajl:
    for nadimak,vrednosti in recnik.items():
        upisni_fajl.write('{:5} {:<3} {}\n'.format(nadimak,vrednosti[0],vrednosti[1]) )
