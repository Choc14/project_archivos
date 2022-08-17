import os

from .models import Customer

class ArchivoCliente:
    customer_list = Customer.objects.all()
    ruta_archivo = 'apps/customers/txt/customers/clientes.txt'

    @classmethod
    def agregar_producto(cls):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            for cliente in cls.customer_list:
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
    def eliminar_producto(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

    @classmethod
    def subir(cls):
        cls.eliminar_producto()
        cls.agregar_producto()

