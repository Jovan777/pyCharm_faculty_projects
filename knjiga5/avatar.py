#potrebno je napraviti upit sa pitanjima kako zelimo da izgleda nas lik
#moguca je default vrednost, ali i mi mozemo da napisemo sta hocemo

def get_attribute(query, default):      #prvo definisemo naziv funkcije i njene parametre(promenljive)
    question=query+' [ '+default+' ]? ' #pravimo lokalnu promenljivu koja sluzi kao pitanje korisniku
    answer=input(question)              #korisnik unosi odgovor
    if answer=='':                      #ako korisnik ne unese nista onda je njegov odgovor default
        answer=default
    print('You chose',answer)         #ispisi sta je korisnik izabrao
    return answer

hair=get_attribute('What color hair?','brown')
hair_length=get_attribute('What hair length?','short')
eyes=get_attribute('What eyes color?','blue')
gender=get_attribute('What gender?','male')
glasses=get_attribute('Has glasses?','no')
beard=get_attribute('Has beard?','no')

