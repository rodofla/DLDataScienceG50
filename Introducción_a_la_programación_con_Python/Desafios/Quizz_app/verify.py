import preguntas as p


def verificar(alternativas, eleccion):
    """
    > The function `verificar` takes in a list of lists (`alternativas`) and a string (`eleccion`) and
    returns a boolean (`correcto`)
    
    The function `verificar` takes in two arguments:
    
    1. `alternativas`: a list of lists
    2. `eleccion`: a string
    
    The function `verificar` returns a boolean:
    
    1. `correcto`: a boolean
    
    :param alternativas: a list of tuples, each tuple containing the text of the answer and a boolean
    value indicating whether it's correct or not
    :param eleccion: the user's choice
    :return: The correct answer is being returned.
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if alternativas[eleccion][1] == 1:
        print('Respuesta Correcta')
        correcto = True
    else:
        print('Respuesta Incorrecta')
        correcto = False 
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






