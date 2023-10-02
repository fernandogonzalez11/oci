def serie(*caps):
    res = 0
    for cap in caps:
        res += 1/cap
    return 1/res

def paralelo(*caps):
    res = 0
    for cap in caps:
        res += cap
    return res

a = serie(6.9, 6.9, 6.9)
b = paralelo(a, 4.6)
c = serie(6.9, 6.9, b)
d = paralelo(4.6, c)
e = serie(6.9, 6.9, d)
print(e)