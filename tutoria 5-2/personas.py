personas = [3, 4, 5, 7, 2]

# suma de prefijos 
prefijos = [0 for i in range(len(personas))]

prefijos[0] = personas[0]

for i in range(1, len(personas)):
    prefijos[i] = prefijos[i-1] + personas[i]

queries = 3

for i in range(queries):
    inicio, fin = map(int, input().split())
    resultado = prefijos[fin]
    if inicio != 0:
        resultado -= prefijos[inicio-1]
    print(resultado)