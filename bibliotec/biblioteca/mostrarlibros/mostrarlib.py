def mostrar_libros(biblioteca):
    '''
        - Descripción:
        Presenta por pantalla los libros introducidos en la biblioteca
        - Entrada de datos:
        none
        - Salida de datos:
        Los libros que están en la biblioteca
    '''
    
    print('\tLista de libros:')
    for libro in biblioteca:
        print(f'\t{libro['titulo']} | {libro['autor']} | {libro['ano']}')

if __name__ == '__main__':
    mostrar_libros()