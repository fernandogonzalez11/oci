n = int(input("deme el numerinho "))

es_primo = True

x = 2
while x**2 <= n:
    if n < 2 or n % x == 0:
        es_primo = False
        break
    
if es_primo:
    print("PRIMO ENCONTRADO!!!!!!! PRIMO!! PRIMO SE ENCONTRÓ!!!!!!")
else:
    print("no encontraste al primo DDDDDDDDDDDDDD:")