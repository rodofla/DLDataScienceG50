# Importing the getpass function from the getpass module and the ascii_lowercase function from the
# string module.
from getpass import getpass
from string import ascii_lowercase as abc

# Asking the user to input a password and then converting it to lowercase.
password = getpass("ingrese su contraseña de letras sin ñ: ").lower()

# Converting the string abc into a list of strings.
list_abc = list(map(str, str(abc)))

# Initializing the variable tries to 0.
tries = 0

# The above code is trying to find the password by comparing each letter of the password with each
# letter of the alphabet.
for i in range(0,len(password)):
    for j in range(0,len(list_abc)):
        if password[i]!=list_abc[j]:
            tries+= 1
        else:
            tries+= 1
            break

# Printing the password and the number of tries it took to find it.
print (f"su contraseña es: {password} y fue adivina en {tries} intentos")
