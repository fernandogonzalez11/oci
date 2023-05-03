edades = [12, 11, 3, 58, 47]
maxima_edad = 0
minima_edad = 200
menor_indice = -1

for edad in edades:
    if edad > maxima_edad:
        print(f"vi que {edad} > {maxima_edad}")
        maxima_edad = edad        
    else:
        print(f"vi que {edad} < {maxima_edad}")

for edad in edades:
    if edad < minima_edad:
        print(f"vi que {edad} < {minima_edad}")
        minima_edad = edad        
    else:
        print(f"vi que {edad} > {minima_edad}")

for i in range(len(edades)):
    if (edades[i] < minima_edad):
        menor_edad = edades[i]
        menor_indice = i

print(maxima_edad)
print(minima_edad)
print(menor_indice)