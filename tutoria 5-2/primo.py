from math import sqrt

n = int(input("deme el numerinho "))
raiz = int(sqrt(n))

es_primo = True
for i in range(2, raiz+1):
    if n < 2 or n % i == 0:
        es_primo = False
        break
    
if es_primo:
    print("PRIMO ENCONTRADO!!!!!!! PRIMO!! PRIMO SE ENCONTRÓ!!!!!!")
else:
    print("no encontraste al primo DDDDDDDDDDDDDD:")