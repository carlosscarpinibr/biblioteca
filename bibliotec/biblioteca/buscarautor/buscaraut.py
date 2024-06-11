def buscar_autor(biblioteca):
    '''
        - Descripción:
        Solicita al usuário que introduzca el nombre del autor que desea buscar en la biblioteca y presenta 
        todos sus libros por pantalla, si no encuentra presenta el mensaje de "Autor no encontrado.".
        - Entrada de datos:
        La variable str autor
        - Salida de datos:
        Presenta los libros del autor introducido por pantalla o el mensaje de "Autor no encontrado.".
    '''

    cont = 0
    autor = input('Entre el nombre del autor que desea buscar: ').lower()
    print(f'\nLista de libros por autor "{autor}" :')
    for libro in biblioteca:
        if libro['autor'] == autor:
            print(f'\t{libro['titulo']} | {libro['autor']} | {libro['ano']}')
            cont = cont + 1
    if cont == 0:
        print('Autor no encontrado.')


if __name__ == '__main__':
    buscar_autor()