def histogram(text):
        p=dict((x,text.count(x)) for x in set(text))

        for i in range(len(p)):
            temp=0
            if ord(p[i][0]) ord(p[i + 1][0]):
                temp = p[i][0]
                p[i][0] = p[i + 1][0]
                p[i + 1][0] = temp
        return p



text = 'abcdefg'
print(histogram(text))