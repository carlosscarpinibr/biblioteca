def entrada_libros():
    '''
        - Descripción:
        Solicita al usuário que introduzca un nombre de un autor, titulo y año.
        - Entrada de datos:
        Las variables str autor y titulo del libro, la variable int para el año del libro.
        Todas con tratamiento contra errores.
        - Salida de datos:
        Una variable dict con los datos introducidos anteriormente.
    '''
    while True:
        autor = input('Entre el nombre del autor: ').lower()
        if autor == '':
            print('El campo no puede estar vacio, intente nuevamente.')
        else:
            break
    while True:
        titulo = input('Entre el título del libro: ').lower()
        if titulo == '':
            print('El campo no puede estar vacio, intente nuevamente.')
        else:
            break
    while True:    
        try:
            ano = int(input('Entre el año del libro: '))
            break
        except ValueError:
            print('Entre un año valido.')

    lib = {'titulo' : titulo, 'autor' : autor, 'ano' : ano}
    return lib

if __name__ == '__main__':
    entrada_libros()