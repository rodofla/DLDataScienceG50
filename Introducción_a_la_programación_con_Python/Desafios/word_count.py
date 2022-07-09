from sys import argv
# function who count a distinct word in a file
lorem = argv[1]


def word_count_distinct():
    try:
        with open(lorem, 'r', encoding="UTF-8") as file:
            char = file.read()
            return len(set(char))
    except FileNotFoundError:
        return 'File not found'
    
def word_count_distinct_2():
    try:
        with open(lorem, 'r', encoding="UTF-8") as file:
            char = file.read()
            return len(set(char.split(" ")))
    except FileNotFoundError:
        return 'File not found'
    

print(f"El número de caracteres distintos es: {word_count_distinct()}")
print (f"El número de palabras distintas es: {word_count_distinct_2()}")


