from math import sqrt

n = int(input("deme el numerinho "))
raiz = int(sqrt(n))

divs = [1, n]

for x in range(2, raiz+1):
    if n % x == 0:
        div1 = x
        div2 = n // x
        divs.append(div1)
        divs.append(div1)
        print(f"el amiguinho {div1} y el {div2}")