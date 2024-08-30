#provera monotonosti sekvence

broj=-float("inf")
while True:
    unos=float(input('Unesite broj: '))
    if broj<unos:
        print('Sekvenca je rastuca ')
    else:
        print('Uneti broj prekida rastucu sekvencu')
        break #kad se unose broj koji prekida sekvencu onda se
              #petlja naglo zavrsava
    broj=unos #obrati paznju kome se dodeljuje vrednost
print('Kraj programa')
