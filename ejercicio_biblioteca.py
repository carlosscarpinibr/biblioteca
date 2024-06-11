from biblioteca.entrarlibro.entralib import entrada_libros
from biblioteca.eliminarlibro.eliminalib import eliminar_libros
from biblioteca.buscarautor.buscaraut import buscar_autor
from biblioteca.mostrarlibros.mostrarlib import mostrar_libros
from biblioteca.verificarbiblioteca.verificabibl import verifica_bibl

libro = {}
biblioteca = []

def principal():

    prompt = '''
            Menu biblioteca
            1. Añadir un nuevo libro
            2. Mostrar todos los libros
            3. Buscar libros por autor
            4. Eliminar un libro
            5. Salir
'''
    opcion = 0

    while opcion != '5':
        print(prompt)
        opcion = input('Entre una opción del menu: ')
        if opcion == '1':
            lib = entrada_libros()
            biblioteca.append(lib)
        elif opcion == '2': # Mostrar todos los libros
            print('Menu 2')
            if verifica_bibl(biblioteca):
                mostrar_libros(biblioteca)
        elif opcion == '3': # Buscar libros por autor
            if verifica_bibl(biblioteca):
                buscar_autor(biblioteca)
        elif opcion == '4': # Eliminar un libro
            if verifica_bibl(biblioteca):
                eliminar_libros(biblioteca)
        elif opcion == '5': # Salir
            print('Fin del programa')
        else:
            print('Opcion inválida')

# llama principal()
principal()
