q = int(input())

for i in range(q):
    a, b, c, p = map(int, input().split())

    def ok(r):
        return a*r + b*(r**2) + c*(r**3) >= p**2

    def busqueda_binaria(low, high, ok):
        high += 1

        while low < high:
            mid = (low + high) // 2
            if ok(mid):
                high = mid
            else:
                low = mid + 1

        return low

    print(busqueda_binaria(1, 10**8, ok))