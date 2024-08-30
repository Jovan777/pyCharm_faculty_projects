
words=input().split('-')
'''
lenghts=[len(word) for word in words]
maximimum_lenght=max(lenghts)
longest_word=[word for word in words if len(word)==maximimum_lenght]
print(longest_word)

if maximimum_lenght==1:
    print('Duzina reci je jedno slovo')
else:

    print('Duzina reci je {} slova'.format(maximimum_lenght))
'''''
lenght=''
for word in words:
    if len(word)>len(lenght):
        lenght=word

print(lenght)