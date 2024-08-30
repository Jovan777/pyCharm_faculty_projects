#napraviti program koji za unetu vrednost a(duzina ivice kocke) racuna povrsinu i
# zapreminu kocke, kao i poluprecnik upisane sfere

#poluprcnik upisane sfere je ru=a/2
#povrsina kocke je P=6a^2
#zapremina kocke je V=a^3


a=int(input('Unesite duzinu ivice kocke: '))
ru=int(a/2)
P=6*a**2
V=a**3

print('Duzina poluprecnika upisane sfere je ', ru)
print('Povrsina kocke je ', P)
print('Zapremina kocke je ', V)