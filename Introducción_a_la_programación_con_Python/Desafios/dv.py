# Importing the cycle function from the itertools module.
from itertools import cycle

# Asking the user to input a number and then converting it to an integer.
rut = int(input("Ingrese su rut sin digito verificador: "))

def digito_verificador(rut):
    """
    It takes the RUT, reverses it, multiplies each digit by a factor, and then sums the results
    
    :param rut: The RUT number you want to validate
    :return: The remainder of the division of the sum of the products of the reversed digits and the
    factors by 11.
    """
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11


dv = digito_verificador(rut)

# The function digito_verificador returns the remainder of the division of the sum of the products of
# the reversed digits and the factors by 11. If the remainder is 10, the digit verificator is "k", and
# if it is 11, the digit verificator is 0.
if dv == 10:
    dv = "k"
elif dv == 11:
    dv = 0

# Printing the RUT number and the digit verificator.
print(f"Su rut es: {rut}-{dv}")
