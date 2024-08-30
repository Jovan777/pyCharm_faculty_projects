broj ,suma = 0,0
while True:
    izbor = int(input("Izbor: "))
    if izbor == 0:
        broj = int(input("Unesi broj: "))
    elif izbor == 1:
        suma += broj
    elif izbor == 2:
        print("Suma: ", suma)
    elif izbor == 3:
# opcija ce biti implementirana kasnije
        pass
    elif izbor == 4:
        break
    else:
        print("Nedozvoljen izbor!")
print(suma)
print("Kraj programa!")