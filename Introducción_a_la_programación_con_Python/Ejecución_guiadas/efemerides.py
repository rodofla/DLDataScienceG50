
# definimos el diccionario
efemerides = {
'1 de Enero': 'Año Nuevo',
'27 de Febrero': 'Terremoto en Chile',
'8 de Marzo': 'Día de la Mujer',
'21 de Mayo': 'Glorias Navales',
'18 de Septiembre': 'Fiestas Patrias',
'19 de Septiembre': 'Glorias del Ejercito',
'25 de Diciembre': 'Navidad'}

# a function who lowercase the keys of the efemerides dictionary
efemerides = {key.lower(): value for key, value in efemerides.items()}


fecha = input("Ingrese una fecha: ").lower()


print(f"Efemérides: {efemerides.get(fecha, 'No hay efemérides para esa fecha')}")
print(efemerides)