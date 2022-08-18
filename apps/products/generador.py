import os



class ArchivoProducto:
    
    ruta_archivo = 'apps/products/txt/products/producto.txt'

    @classmethod
    def agregar_producto(cls, Product):
        product_list = Product.objects.all()

        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            for producto in product_list:
                archivo.write(f'{producto.id}'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Nombre del producto: {producto.title}\n')
                archivo.write(f'Descripcion: {producto.description}\n')
                archivo.write(f'Price: {producto.price}\n')
                archivo.write(f'Categoria: {producto.category}\n')
                
                    
                
                fecha = producto.created_at.strftime('%Y-%m-%d')
                archivo.write(f'Fecha de creacion: {fecha}\n')
                archivo.write(f'\n')


    @classmethod
    def eliminar_producto(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

    @classmethod
    def subir(cls, Product):
        cls.agregar_producto(Product)
        cls.eliminar_producto()
        cls.agregar_producto(Product)

