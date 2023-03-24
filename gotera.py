def transformar(cantidad):
    horas = cantidad // 3600
    cantidad -= horas * 3600
    minutos = cantidad // 60
    cantidad -= minutos * 60
    print(f'{stringify(horas)}:{stringify(minutos)}:{stringify(cantidad)}')

def transformarFormato(casosPrueba):
    # entre 0 (incluido) y casosPrueba (excluido)
    for i in range(0, casosPrueba):
        cantidadSegundos = int(input("Cantidad de segundos: "))
        transformar(cantidadSegundos)

def stringify(numero):
    if numero < 10:
        return f"0{numero}"
    else:
        return str(numero)

cantidadCasos = int(input("Ingrese cantidad de casos de prueba: "))
transformarFormato(cantidadCasos)