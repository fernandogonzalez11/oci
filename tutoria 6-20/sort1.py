def bin_search(lo, hi, ok):
    hi += 1
    while lo < hi:
        mid = (lo+hi)//2
        if not ok(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo

def ok(x):
    return x**2 >= n

n = 26 

print(bin_search(0, n, ok))