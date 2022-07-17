from pprint import pprint

umbral=int(input("Ingrese Umbral: "))

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

#Imprimimos el resultado
mayor_a = {key:value for (key, value) in ventas.items() if value > umbral}
print(f'El/los meses con ventas mayor a ${umbral} es/son:\n')
pprint(mayor_a, sort_dicts=False)