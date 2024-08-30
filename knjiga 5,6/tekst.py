import ch1tekst

#sada je potrebno napraviti funkciju koja ce izracuna broj reci, broj recenica i broj slogova i izracunati citljivost

def count_sylabless(words):
    count=0
    for word in words:
        word_count=count_sylabless_in_word(word)
        count+=word_count
    return count


def count_sylabless_in_word(word):
    count=0
    last_char=word[-1]
    endings_of_word='.!,;?:'
    posible_e='eE'
    if last_char in endings_of_word:
        procesed_word=word[:-1]
    else:
        procesed_word=word
    if procesed_word[-1] in posible_e:
        procesed_word=procesed_word[:-1]

    if len(procesed_word)<=3:
        return 1
    samoglasnici='aeiouAEIOU'
    prev_char_was_s=False
    for char in procesed_word:
        if char in samoglasnici:
            if not prev_char_was_s:
                count+=1
            prev_char_was_s=True
        else:
            prev_char_was_s=False

    if procesed_word[-1] in 'Yy':
        count+=1

    return count

def output_results(score):
    if score>=90:
        print('Nivo citljivosti za 5. razred')
    elif score>=80:
        print('Nivo citljivosti za 6. razred')
    elif score>=70:
        print('Nivo citljivosti za 7. razred')
    elif score>=60:
        print('Nivo citljivosti za 8. razred')
    elif score>=50:
        print('Nivo citljivosti za srednju skolu')
    elif score>=40:
        print('Nivo citljivosti za studente')
    else:
        print('Nivo citljivosti visokoobrazovane ljude')

def count_sentences(tekst):
    count=0
    terminals='.!?;'
    for char in tekst:
        #if char=='.' or char=='!' or char=='?' or char==';':
        if char in terminals:
           count=count+1
    return count

def compute_readability(tekst):
    total_words=0
    total_sentences=0
    total_syllables=0
    score=0
    words=tekst.split()
    total_words=len(words)
    print('Broje reci je:{}'.format(total_words))
    total_sentences=count_sentences(tekst)
    print('Broj recenica je:{}'.format(total_sentences))
    total_syllables=count_sylabless(words)
    print('Broj slogova je:{}'.format(total_syllables))
    score=(206.835-1.015*(total_words/total_sentences)
           -84.6*(total_syllables/total_words))
    print('Rezultat je:{:.2f}'.format(score))
    output_results(score)

q=compute_readability(ch1tekst.tekst)
print(q)



