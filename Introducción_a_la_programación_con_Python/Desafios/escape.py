from math import sqrt # Importa la función sqrt de la librería math
from os import system # Importa os.system para limpiar la pantalla


def clear():
    """
    It clears the terminal screen
    """
    system('clear')

# Menú con las instrucciones del programa
def menu():
    print("""
                    ¡¡¡¡Bienvenido!!!

Aquí podras calcular la velocidad de escape del planeta Tierra.

La velocidad de escape de un planeta se define como la mínima 
velocidad necesaria para salir de un planeta venciendo la gravedad.

La velocidad de escape se calcula mediante la siguiente fórmula:

                    Ve = sqrt(2 * g * r)

Ve: corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s²].
r: Corresponde al radio del planeta en [m].

Recuerde:
1.- Ingrese el radio en Km.
2.- Ingrese el valor de la gravedad en m/s².

""")


menu()


# Inputs validando que sean números decimales.
while True:
    try:
        c_gravitacional = float(input("¿Cúal es el valor de la constate gravitacional?\n >> "))  
    except ValueError:
        clear()
        menu()
        print("\nDebes ingresar la constante con sus decimales!\n")
        continue
    else:
        clear()
        menu()
        break
    

while True:
    try:
        radio = int(input("¿Cúal es el radio del planeta Tierra?\n >> "))*1000
    except ValueError:
        clear()
        menu()
        print("Debe ingresar solo valores numéricos enteros\n")
        continue
    else:
        clear()
        menu()
        break
    

# Calcula la velocidad de escape
velocidad_escape = sqrt(2 * (c_gravitacional * radio))


#Outputs
print(f"La velocidad de escape del planeta Tierra es {velocidad_escape:,.1f} [m/s]\n")
