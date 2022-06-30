# importa librería math
import math


# Solicitud de Inputs
proteina = float(input("Ingrese la cantidad de proteina:\n> "))
carbohidratos = float(input("Ingrese la cantidad de carbohidratos:\n> "))
grasa = float(input("Ingrese la cantidad de grasa:\n> "))


# cálculo de calorías
calorias = math.ceil(4 * proteina + 4 * carbohidratos + 9 * grasa)


# entregar output en el formato solicitado  
print(f"Las calorías totales del producto son: {calorias}")