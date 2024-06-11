def verifica_bibl(biblioteca):
    '''
        - Descripción:
        Verifica si la biblioteca está vácia
        - Entrada de datos:
        none
        - Salida de datos:
        Si esta vacía, presenta un mensaje en pantalla o restorna True
    '''
    
    if len(biblioteca) == 0:
        print('La biblioteca está vacía')
    else:
        return True

if __name__ == '__main__':
    verifica_bibl()