
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]


def promedio(lista):
    return sum(lista)/len(lista)


def filtrar(velocidad):
    media = promedio(velocidad)
    above_average_values = [i for i, v in enumerate(velocidad) if v > media]
    return above_average_values 

lista_final = filtrar(velocidad) # Lista con los indices de los valores mayores al promedio


resulado = """las posiciones de las correas que están sobre el promedio 
de consumo energetico son: \n""", *lista_final

print(*resulado) # Imprime la lista con los indices de los valores mayores al promedio