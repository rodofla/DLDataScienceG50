from encodings import utf_8
from sys import argv # Importamos la librería argv para agregar los argumentos por línea de comandos

# variables que reciben los argumentos
lorem = argv[1]

# función que que cuenta la cantidad de caracteres distintos en el archivo
def char_count_distinct():
    try:
        with open(lorem, 'r', encoding="UTF-8") as file:
            char = file.read()
            return len(set(char))
    except FileNotFoundError:
        return 'File not found'
 
# función que cuenta la cantidad de palabras distintas en el archivo   
def word_count_distinct():
    try:
        with open(lorem, 'r', encoding="UTF-8") as file:
            words = file.read()
            return len(set(words.split(" ")))
    except FileNotFoundError:
        return 'File not found'
    


print(f"""
      Bienvenido a la aplicación de conteo de palabras
      y caracteres en el archivo de texto: {lorem}
                espero que te guste.\n""")


print(f"El número de caracteres distintos es: {char_count_distinct()}")
print (f"El número de palabras distintas es: {word_count_distinct()}")
