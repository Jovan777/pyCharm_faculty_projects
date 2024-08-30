def najduzipodniz(s):
    najduzi_podniz= ''
    i = 0
    while (i < len(s)):
        trenutni_niz = ''

        while (i < len(s) and s[i].isalpha() and s[i].islower()):
            trenutni_niz += s[i]
            i += 1

        if (i < len(s) and not (s[i].islower())):
            i += 1

        if (len(trenutni_niz) >= len(najduzi_podniz)):
            najduzi_podniz = trenutni_niz

    return najduzi_podniz

reci=input().split('-') #abc1d2ef3g0
slova=[]
for slovo in reci:
    slova.append(slovo)
ispis=''
for i in range(len(slova)):
    ispis+=najduzipodniz(slova[i])

print(ispis,end="")