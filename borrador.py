import os

from func.funciones.menu import *

def main():
    
    '''
    Funcion en donde desplaza un menu.
    '''
    
    print('Elige una opcion'.center(60,'-'))
    
    decide = int(input(f'''
    1) Borrar las bases de datos
    2) Crear respaldo de alguna base de datos
    3) Restablecer datos   
    0) Salir    
    '''))
    os.system('cls')
    

    if decide == 1:
        borrar()

    elif decide == 2:
        respaldo()

    elif decide == 3:
        restablecer()
   
    elif decide == 0:
        print('adios')
        os.system('cls')
    else:
        print('Error')



if __name__ == '__main__':
    
    main()