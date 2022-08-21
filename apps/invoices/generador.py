import os
from django.db.models import Q


class ArchivoFacturas:
    
    ruta_archivo = 'apps/invoices/txt/invoices/facturas.txt'

    @classmethod
    def agregar_facturas(cls, Invoice, DetailInvoice):
        invoice_list = Invoice.objects.all()

        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            for factura in invoice_list:
                archivo.write(f'{factura.id}'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Nombre del usuario: {factura.customer}\n')
                fecha = factura.created_at.strftime('%Y-%m-%d')
                archivo.write(f'Fecha de creacion: {fecha}\n')
                archivo.write(f'\n')

                detalle_list = DetailInvoice.objects.filter(Q(invoice=factura.id))
                for detalle in detalle_list:
               
                    archivo.write(f'Nombre del producto: {detalle.product}\n')
                    archivo.write(f'Precio: {detalle.price}\n')
                    archivo.write(f'Cantidad: {detalle.quantity}\n')
                    archivo.write(f'Subtotal: {detalle.subtotal}\n')
                    archivo.write(f'\n')
                    archivo.write(f'\n')

                archivo.write(f'-'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Subtotal: {factura.subtotal}\n')
                archivo.write(f'IVA calculado: {factura.iva}\n')
                archivo.write(f'-'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'-'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Total: {factura.total}\n')
                archivo.write(f'\n')


    @classmethod
    def eliminar_facturas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

    @classmethod
    def subir(cls, Invoice, DetailInvoice):
        cls.agregar_facturas(Invoice,DetailInvoice)
        cls.eliminar_facturas()
        cls.agregar_facturas(Invoice,DetailInvoice)
