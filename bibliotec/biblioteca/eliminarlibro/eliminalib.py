def eliminar_libros(biblioteca):
    '''
        - Descripción:
        Solicita al usuário que introduzca un nombre del libro que desea eliminar de la biblioteca,
        busca por el titúlo en la biblioteca y lo elimina.
        - Entrada de datos:
        La variable str elimina, que reciberá el nombre del libro y lo buscara en la list biblioteca.
        Todas con tratamiento contra errores.
        - Salida de datos:
        Cuando encuentra el titulo en la list biblioteca, elimina el dict correspondiente.
    '''
    elimina = input('Entre el titulo del libro que desea eliminar: ').lower()
    for i, libro in enumerate(biblioteca):
        for key, titulo in libro.items():
            if libro['titulo'] == elimina:
                #print(f'{key} : {titulo}')
                aux = i
    while True:    
        try:
            del biblioteca[aux]
            print(f'{elimina} fue eliminado.')
            break
        except UnboundLocalError:
            print('El titulo introducido no existe')
            break


if __name__ == '__main__':
    eliminar_libros()