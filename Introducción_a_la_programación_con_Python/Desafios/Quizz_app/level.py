def choose_level(n_pregunta, p_level):
    # Construir lógica para escoger el nivel
    
    if p_level == 1:
        n_pregunta = 3
        while n_pregunta <= 3:
            level = 'basicas'
    elif p_level == 2:
        n_pregunta = 6
        while n_pregunta <= 2:
            level = 'basicas'
            while 2 < n_pregunta <= 4:
                level = 'intermedias'
                while 4 < n_pregunta <=6:
                    level = 'avanzadas'
    else:
        n_pregunta = 9
        while n_pregunta <= 3:
            level = 'basicas'
            while 3 < n_pregunta <= 6:
                level = 'intermedias'
                while 6 < n_pregunta <= 9:
                    level = 'avanzadas'
        
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias