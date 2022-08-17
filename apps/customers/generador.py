import os



class ArchivoCliente:
    
    ruta_archivo = 'apps/customers/txt/customers/clientes.txt'

    @classmethod
    def agregar_cliente(cls, Customer):
        customer_list = Customer.objects.all()

        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            for cliente in customer_list:
                archivo.write(f'{cliente.id}'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Nombre del cliente: {cliente.first_name}\n')
                archivo.write(f'Apellido del cliente: {cliente.last_name}\n')
                archivo.write(f'Direccion: {cliente.addres}\n')
                archivo.write(f'Numero de telefono: {cliente.phone_number}\n')
                cumple = cliente.date_birth.strftime('%Y-%m-%d')
                archivo.write(f'Fecha de cumpleaños: {cumple}\n')
                archivo.write(f'Ciudad: {cliente.city}\n')
                archivo.write(f'Identificador: {cliente.id_type}\n')
                
                fecha = cliente.created_at.strftime('%Y-%m-%d')
                archivo.write(f'Fecha de creacion: {fecha}\n')
                archivo.write(f'\n')


    @classmethod
    def eliminar_cliente(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

    @classmethod
    def subir(cls, Customer):
        cls.agregar_cliente(Customer)
        cls.eliminar_cliente()
        cls.agregar_cliente(Customer)

