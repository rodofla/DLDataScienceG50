from sys import argv # Importamos la librería argv
from xmlrpc.client import boolean   # importa el módulo argv


# variables que reciben los argumentos
sol = float(argv[1])
arg = float(argv[2])
usd = float(argv[3])
clp = int(argv[4])

# calculando la conversión
sol_clp =  sol * clp
arg_clp =  arg * clp
usd_clp =  usd * clp

# imprime el resultado
print(f"""
Los {clp} equivalen a:
{sol_clp:.1f} Soles
{arg_clp:.1f} Pesos Argentinos
{usd_clp:.1f} Dolares


""")

