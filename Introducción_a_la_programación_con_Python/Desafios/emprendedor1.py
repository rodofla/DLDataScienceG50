import os # To clear the screen

def clear():
    """
    It clears the terminal screen
    """
    os.system('clear')


def menu():
    print("""
Bienvenido al programa de emprendedor
Aquí podrás calcular tus utilidades.

Recuerda solo ingresar números enteros.   
""")


# Inputs validando que sean números enteros
while True:
    clear()
    menu()
    try:
        valor_suscripcion = int(input("¿Cúal es el valor de la suscripción?\n >> "))  
    except ValueError:
        print("El valor de la suscipción debe ser un número entero\n")
        continue
    else:
        break
    
    
while True:
    clear()
    menu()
    try:
        usuarios = int(input("\n¿Cúal es el número de usuarios?\n >> "))
    except ValueError:
        print("El número de usuarios debe ser un número entero\n")
        continue
    else:
        break
    
    
while True:
    clear()
    menu()
    try:
        gastos_totales = int(input("\n¿Cúal es el gasto total?\n >> "))
    except ValueError:
        print("El gasto total debe ser un número entero\n")
        continue
    else:
        clear()
        menu()
        break

# Cálculo de utilidades
utilidades = valor_suscripcion * usuarios - gastos_totales

# Output
print(f"\nLas utilidades son: ${utilidades:,} pesos ")    


