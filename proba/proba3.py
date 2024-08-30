#ispisi da li je korisnik samo polozio(nezavisno od ocene) ili da je pao

p=int(input('Unesite osvojeni broj poena'))

# na dva nacina radimo

if p>50:
    print('Polozili ste ispit')
else:
    print('Niste polozili ispit')

poruka='Da' if p>50 \
            else 'Ne' # ne dodaje se fazon poruka=....
print('Polozio:',poruka)