#program prebrojava karaktere u ispisanoj reci

brojVslova=0
brojMslova=0
brojbrojeva=0
brojostalih=0


while(True):
    word=input()
    if len(word)==0:
        break
    for znak in word:
        if (ord('a') <= ord(znak) <= ord('z')):
            brojMslova=brojMslova+1
        elif (ord('A') <= ord(znak) <=ord('Z')):
            brojVslova=brojVslova+1
        elif (ord('0')<=ord(znak) <= ord('9')):
            brojbrojeva=brojbrojeva+1
        else:
            brojostalih=brojostalih+1

print(brojostalih,brojbrojeva,brojVslova,brojMslova)
