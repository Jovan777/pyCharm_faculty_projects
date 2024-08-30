def povrsina (a = 0, b = 0, c = 0):
    if a and b and c:
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5
    elif a and b:
        return a * b
    elif a:
        return a * a
    else:
        return 0

z=povrsina(c = 5, b = 6, 10)
print(z)