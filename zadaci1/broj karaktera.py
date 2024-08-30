tekst='''Nikola Tesla (Smiljan, 10. jul 1856 — Njujork, 7. januar 1943) bio je srpski i američki[1][2][3] pronalazač, inženjer elektrotehnike i mašinstva i futurista, najpoznatiji po svom doprinosu u projektovanju modernog sistema napajanja naizmeničnom strujom.

Najznačajniji Teslini pronalasci su polifazni sistem, obrtno magnetsko polje, asinhroni motor, sinhroni motor i Teslin transformator. Takođe, otkrio je jedan od načina za generisanje visokofrekventne struje, dao je značajan doprinos u prenosu i modulaciji radio-signala, a ostali su zapaženi i njegovi radovi u oblasti rendgenskih zraka.

Njegov sistem naizmeničnih struja je omogućio znatno lakši i efikasniji prenos električne energije na daljinu. Bio je ključni čovek u izgradnji prve hidrocentrale na Nijagarinim vodopadima.

Preminuo je u svojoj 87. godini, siromašan i zaboravljen.

Jedini je Srbin po kome je nazvana jedna međunarodna jedinica mere, jedinica mere za gustinu magnetnog fluksa ili jačinu magnetnog polja — tesla.

Nikola Tesla je autor više od 700 patenata, registrovanih u 25 zemalja, od čega u oblasti elektrotehnike 112.'''
'''
brojmalih=0
brojvelikih=0
brojcifara=0
brojostalih=0
'''
def brojznakova(tekst):
    brojmalih = 0
    brojvelikih = 0
    brojcifara = 0
    brojostalih = 0
    for znak in tekst:
        if (ord('a') <= ord(znak) <= ord('z')):
            brojmalih+=1
        elif (ord('A') <= ord(znak) <= ord('Z')):
            brojvelikih+=1
        elif (ord('0') <= ord(znak) <= ord('9')):
            brojcifara+=1
        else:
            brojostalih+=1
    print(brojmalih,brojvelikih,brojcifara,brojostalih)

def pojavljivanje_znaka(slovo,tekst,defslovo):
    brojac=0
    pojavljivanje=0
    while brojac<len(tekst):
        for slovo in tekst:
            if defslovo==slovo:
                pojavljivanje+=1
            brojac+=1
    return pojavljivanje

def ceo_tekst(tekst):
    alphabet=['a','b','c','z','e','r','t','q','s','d','f','g','h','j','k','l','x','v','m','n','y','u','i','o','p','w']
    brojac=0
    while brojac<len(tekst):
        for i in range(len(tekst)):
            print(pojavljivanje_znaka(tekst[i],tekst,alphabet[i]))
        brojac+=1




a=ceo_tekst(tekst)
print(a)
