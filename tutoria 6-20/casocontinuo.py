def bin_search(lo, hi, ok):
    for i in range(200):
        mid = (lo+hi)/2
        if not ok(mid):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

n = 30

def posible_raiz(x):
    return x*x >= n

res = bin_search(0, n, posible_raiz)
print(res*res)