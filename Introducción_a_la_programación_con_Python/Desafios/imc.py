print("""    Bienvenido a la calculadora de IMC
escriba su peso en kg y su altura en metros\n""")

# Variables y su inicialización por inputs
w = int(input("Ingrese su peso en kg: "))
h = (float(input("Ingrese su altura en metros: ")))**2

# Calculo del IMC
imc = w / h

# Definir el rango del IMC
if imc < 18.5:
    estado = "Bajo peso"
elif 18.5 <= imc < 25:
    estado = "Adecuado"
elif 25 <= imc < 30:
    estado = "Sobrepeso"
elif 30 <= imc < 35:
    estado = "Obesidad grado I"
elif 35 <= imc < 40:
    estado = "Obesidad grado II"
else:
    estado = "Obesidad grado III"
    

# Imprimir resultados
print(f"\nSu IMC es: {imc:.2f}")
print(f"La clasificación OMS es {estado}")



