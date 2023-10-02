####### rangos 1D ######

nums = [-3, 2, 5, 7, 15, 10, 11, -7, 3, 1]
prefijos = [nums[0]]

def hacerPrefijos():
    for i in range(1, len(nums)):
        prefijos.append(prefijos[-1] + nums[i])

def sumaRango(inicio, fin):
    suma = prefijos[fin]
    if inicio != 0:
        suma -= prefijos[inicio-1]
    
    return suma

hacerPrefijos()
print(prefijos)
print(sumaRango(2, 7))

####### rangos 2D ######
mat = [
    [-3,  2,  5,  7],
    [15, 10, 11, -7],
    [6,  3,   1,  4]
]
prefijos = [ [0 for i in range(len(mat[0]))] for j in range(len(mat)) ]


# (fila, columna)
def sumaRango2D(inicio, fin):
    suma = prefijos[fin[0]][fin[1]]

    if inicio[0]:
        suma -= prefijos[inicio[0] - 1][fin[1]]
    
    if inicio[1]:
        suma -= prefijos[fin[0]][inicio[1] - 1]

    if inicio[0] and inicio[1]:
        suma += prefijos[inicio[0] - 1][inicio[1] - 1]
    
    return suma

def hacerPrefijos():
    prefijos[0][0] = mat[0][0]
    for fila in range(1, len(mat)):
        prefijos[fila][0] = prefijos[fila-1][0] + mat[fila][0]
        
    for columna in range(1, len(mat[0])):
        prefijos[0][columna] = prefijos[0][columna-1] + mat[0][columna]

    for fila in range(1, len(mat)):
        for columna in range(1, len(mat[0])):
            prefijos[fila][columna] = prefijos[fila-1][columna] + prefijos[fila][columna-1] - prefijos[fila-1][columna-1] + mat[fila][columna]

hacerPrefijos()
print(prefijos)

print(sumaRango2D(
    (0, 0),
    (1, 1)
))