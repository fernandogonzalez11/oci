# yo soy
# yo soy
# yo soy
# yo soy
# yo soy
# yo soy
# yo soy


# yo soy
# yo soy




# yo soy


# yo soy
# yo soy
# yo soy




# yo soy

































nums = [-3, 2, 5, 7, 15, 10, 11, -7, 3, 1]

def sumaMaximaIneficiente(arr):
    respuesta = 0
    respuestaCoord = (0, 0)
    for i in range(len(arr)):
        suma = 0
        for j in range(i, len(arr)):
                suma += arr[j]
                if suma > respuesta:
                    respuesta = suma
                    respuestaCoord = (i, j)
                
    return respuesta, respuestaCoord

def sumaMaxima(arr):
    respuesta = 0
    sumaActual = 0
    for i in range(len(nums)):
        if sumaActual < 0:
            sumaActual = nums[i]
        else:
            sumaActual += nums[i]

        respuesta = max(sumaActual, respuesta)

    return respuesta

print(sumaMaxima(nums))


mat = [
    [-3,  2,  5,  7],
    [15, 10, 11, -7],
    [6,  3,   1,  4]
]
filas = len(mat)
columnas = len(mat[0])
def sumaMaxima2D_fuerzaBruta(matriz):
    resultado = 0
    suma = 0
    # lol
    for f1 in range(filas):
        for c1 in range(columnas):
            for f2 in range(f1, filas):
                for c2 in range(c1, columnas):
                    suma = 0
                    for fila in range(f1, f2+1):
                        for columna in range(c1, c2+1):
                            suma += matriz[fila][columna]
                            resultado = max(resultado, suma)
    return resultado

def sumaMaxima2D_fuerzaBruta2(matriz):
    resultado = 0
    suma = 0
    # lol
    for f1 in range(filas):
        for f2 in range(filas):
            for c1 in range(f1, columnas):
                for c2 in range(c1, columnas):
                    suma = 0
                    for fila in range(f1, f2+1):
                        for columna in range(c1, c2+1):
                            suma += matriz[fila][columna]
                            resultado = max(resultado, suma)
    return resultado

print(sumaMaxima2D_fuerzaBruta(mat))


### eficiente n^3:
# hacer suma de prefijos por fila, para cada fila
# probar todas las longitudes en una fila posible
# obtener suma de la subfila con los prefijos, para cada fila
# obtener mayor suma para las columnas con esta longitud ^ predeterminada
# comparar con máximo