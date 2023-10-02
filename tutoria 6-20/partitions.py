def bin_search(lo, hi, ok):
    hi += 1
    while lo < hi:
        mid = (lo+hi)//2
        if not ok(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo

def es_posible(articulos, cantidad_cargueros, limite):
    n = len(articulos)
    conteo_cargueros = 0
    i = 0
    while i < n:
        suma_actual = articulos[i]
        i+=1
        while i < n and suma_actual + articulos[i] <= limite:
            suma_actual += articulos[i]
            i+=1
        conteo_cargueros += 1
    
    if conteo_cargueros > cantidad_cargueros:
        return False
    return True


def minima_suma_de_carga(articulos, cantidad_cargueros):
    lo = max(articulos)
    hi = sum(articulos)

    def ok(x):
        return es_posible(articulos, cantidad_cargueros, x)
    r = bin_search(lo, hi, ok)
    if r <= hi:
        return r
    return -1

arts = [1, 2, 1000, 5]
print(minima_suma_de_carga(arts, 2))