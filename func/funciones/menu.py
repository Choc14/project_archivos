import os
from .rutas import *

def borrar():
    print('ESTA SEGURO QUE QUIERE REALIZAR LA SIGUIENTE OPERACION'.center(75,'*'))
    decidir = input('Digite y/N: ')

    if decidir == 'y' or decidir == 'Y':
        print('Ahora se esta realizando el proceso'.center(75,'*'))

        for delete in rutas:
            os.remove(delete)

        os.system('cls')
        print('Trabajo hecho'.center(75,'*'))
        

    elif decidir=='n' or decidir=='N':
        os.system('cls')
        print('ADIOS'.center(75,'*'))
        
    else:
        os.system('cls')
        print('NO VALIDO'.center(75,'*'))