
#potrebno je napraviti program koji proverava da li je uneta recenica palindrom

def prepare_sentece(s):
    return  s.lower().strip().replace(" ","") #uklanja bele znakove i menja ih onim cime mi zelimo
            #lower pretvara sve znakove u mala slova, strip menja bele znakove

def isPalindrome(s):
    prepared=prepare_sentece(s)
    for i in range (len(prepared)//2):
        if prepared[i]==prepared[-i-1]:
            return True
        else:
            return False

n=isPalindrome('Evo love')
print(n)

#palindrom reversed
def palindrom_reversed(string):
    for p,q in zip(string,reversed(string)):
        if p!=q:
            return False
        else:
            return True

n=palindrom_reversed(prepare_sentece('Ana voli Milovana'))
print(n)

def isPalindromeSlice(s):
    return s==s[::-1]

z=isPalindromeSlice(prepare_sentece('Evo Love'))
print(z)


