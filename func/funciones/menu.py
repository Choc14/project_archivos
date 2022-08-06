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

def menu():
    print(f'''
    1) Todos
    2) products
    3) invoices
    4) customers
    5) users
    
    ''')

def respaldo():
    '''
    Crea un backup
    '''
    print('A que modelo quiere crear un backup de los datos'.center(60,'-'))
    menu()

    opcion = int(input('Digite la opcion: '))
    if opcion == 1:
        #Todos
        for backup in rutas1:
            os.system(backup)
        os.system('cls')

    elif opcion == 2:
        #products 
        os.system(rutas1[0])
        os.system(rutas1[1])        
        os.system('cls')

    elif opcion == 3:
        #invoices 
        print('Aun no hay modelo hecho')      
        os.system('cls')

    elif opcion == 4:
        #customers

        print(f'''
        1) Quiere Respaldar Todo
        2) Quiere Respaldar Identificadores y Ciudad
        3) Quiere Respaldar Ciudad
        4) Quiere Respaldar Identificadores
        5) Quiere Respaldar Clientes        
        ''')
        
        opt = int(input('Digite una opcion: '))

        if opt == 1:
            os.system(rutas1[2])
            os.system(rutas1[3])
            os.system(rutas1[4])

        elif opt == 2:
            os.system(rutas1[2])
            os.system(rutas1[3])

        elif opt == 3:
            os.system(rutas1[2])

        elif opt == 4:
            os.system(rutas1[3])

        elif opt == 5:
            os.system(rutas1[4])
        else:
            print('Error'.center(60,'-'))

        os.system('cls')

    elif opcion == 5:
        #users 
        os.system(rutas1[5])
        os.system('cls')
        
          

     
    else:
        os.system('cls')
        print('ERROR')

def restablecer():
    print('A que modelo quiere restablecer los datos'.center(60,'-'))
    menu()

    opcion = int(input('Digite la opcion: '))
    if opcion == 1:
        #Todos
        for backup in rutas2:
            os.system(backup)
        os.system('cls')

    elif opcion == 2:
        #products 
        os.system(rutas2[0]) 
        os.system(rutas2[1])       
        os.system('cls')

    elif opcion == 3:
        #invoices 
        print('Aun no hay modelo')       
        os.system('cls')

    elif opcion == 4:
        #customers 
        print(f'''
        1) Quiere Restablecer Todo
        2) Quiere Restablecer Identificadores y Ciudad
        3) Quiere Restablecer Ciudad
        4) Quiere Restablecer Identificadores
        5) Quiere Restablecer Clientes        
        ''')
        
        opt = int(input('Digite una opcion: '))

        
        if opt == 1:
            os.system(rutas2[2])
            os.system(rutas2[3])
            os.system(rutas2[4])

        elif opt == 2:
            os.system(rutas2[2])
            os.system(rutas2[3])

        elif opt == 3:
            os.system(rutas2[2])

        elif opt == 4:
            os.system(rutas2[3])

        elif opt == 5:
            os.system(rutas2[4])

        os.system('cls')

    elif opcion == 5:
        #users 
        os.system(rutas2[5])
        
        os.system('cls')    

     
    else:
        os.system('cls')
        print('ERROR')
