
#lista entregada para desarrollara el ejercicio, se asume que hay que trabajar dentro de este mismo archivo por las
# instrucciones del ejercicio.
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


""" 
1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para
“Empezar el Año”.
"""

recordatorios.insert(1,['2021-02-02', "06:00", "Empezar el Año"])

"""
Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar
de tal manera que sea el 16 de Julio.

"""

recordatorios[3][0] = '2021-07-16'
print('\n'.join(map(str, recordatorios)))
"""
Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del
día del trabajo.

"""
recordatorios.pop(2)

"""
Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a
las 22 hrs.
"""
recordatorios.insert(4,['2021-12-25', "22:00", "Cena de Navidad"])
recordatorios.append(['2022-01-01', "22:00", "Cena de año Nuevo"])

