def bk_r(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bk_r(n - 1, k - 1) + bk_r(n - 1, k)
def pt_bk(n):
    spoljasnja = []
    for i in range(0, n):
        unutrasnja = []
        for j in range(0, i + 1):
            unutrasnja.append(bk_r(i, j))
            spoljasnja.append(unutrasnja)
    return spoljasnja

z=pt_bk(5)
print(z)


q=int(input('Unesite q: '))
pt=pascal_triangle(q)
ppt=printpascalt(pt)

def proba(q):
    while True:
        x = int(input())
        if not 0 <= x <globals(q):
            break;
        o=print(sum(globals(pt[x])))
    return o

m=proba(5)
print(m)
