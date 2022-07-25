from math import prod #import the function prod

#a function who calculate the factoriel of a number
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#a function who calculate the the producer of a list of numbers
def productoria(lista):
    if len(lista) == 0:
        return 1
    else:
        return prod(lista)
    
#a menu who ask the user to choose a number and a list of numbers
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


