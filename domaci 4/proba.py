def krug():
    while True:
        r,x,y,boja=input().split()
        r=int(r)
        if r>0:
            r=int(r)
            xk=int(x)
            yk=int(y)
            bojakruga=str(boja)
            r, x, y, boja = input().split()
            return r,xk,yk,bojakruga
        else:
            break


'''
        r=int(r)
        if r<0:
            break

        else:
            r=int(r)
            xkruga=int(x)
            ykruga=int(y)
            bojakruga=str(boja)
            return r,x,y,boja
        '''
q=krug()
print(q)