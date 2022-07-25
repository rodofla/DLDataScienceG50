from math import prod #import the function prod


def fact(n):
    """
    "If n is 0, return 1, otherwise return n times the factorial of n-1."
    
    The factorial of a number is the product of all the integers from 1 to that number. For example, the
    factorial of 5 is 5*4*3*2*1, which equals 120
    
    :param n: The number to calculate the factorial of
    :return: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def productoria(lista):
    """
    If the list is empty, return 1. Otherwise, return the product of the list.
    
    :param lista: a list of numbers
    :return: The product of the elements in the list.
    """
    if len(lista) == 0:
        return 1
    else:
        return prod(lista)
    

def menu():
    print("""
    ¡¡¡¡Bienvenido!!!
    ¿Qué deseas calcular?
    1. Factorial
    2. Productoria
    3. Salir
    """)
    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Debes ingresar un número entero")
        menu()
    else:
        if opcion == 1:
            try:
                n = int(input("Ingresa un número: "))
            except ValueError:
                print("Debes ingresar un número entero")
                menu()
            else:
                print("El factorial de", n, "es", fact(n))
                menu()
        elif opcion == 2:
            try:
                productoria_string = input("Ingresa una lista de números separados por comas: ")
                productoria_list = productoria_string.split(",")
                productoria_list = [int(i) for i in productoria_list]
            except ValueError:
                print("Debes ingresar una lista de números separados por comas")
                menu()
            else:
                print(f"\nla productoria de {productoria_list} es {productoria(productoria_list)}") 
                menu()
        elif opcion == 3:
            print("Gracias por usar nuestro programa")        


menu ()


