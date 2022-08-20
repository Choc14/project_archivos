###------CREACION DE LAS CLASES CORRESPONDIENTES AL MODULO CON SUS RESPECTIVAS
# VARIABLES, METODOS-----###

from apps.customers.clases.customers import Clientes

class Factura(Clientes):

    def __init__(self, city,id_type, first_name, last_name,address,phone_number, date_birth, id,iva, subtotal, total, created_at ):
 
        super().__init__(city,id_type,first_name, last_name,address,phone_number, date_birth)
        self.__id = id        
        self.__iva = iva
        self.__subtotal = subtotal
        self.__total = total
        self.__creacion = created_at

    @property
    def id(self):
        return self.__id
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def iva(self):
        return self.__iva
    
    @property
    def subtotal(self):
        return self.__subtotal
    
    @property
    def total(self):
        return self.__total
    
    @property
    def fecha(self):
        return self.__creacion

    @id.setter
    def id(self, id):
        self.__id = id

    @iva.setter
    def iva(self, iva):
        self.__iva = iva

    @subtotal.setter
    def subtotal(self, subtotal):
        self.__subtotal = subtotal

    @total.setter
    def total(self, total):
        self.__total = total

    @created_at.setter
    def subtotal(self, created_at):
        self.__creacion = created_at
    
    def __str__(self) -> str:
        return f'''
        No. {self.__id}
        Cliente: {super().nombre}
        IVA: {self.__iva}
        SUBTOTAL: {self.__subtotal}
        TOTAL: {self.__total}
        FECHA DE CREACION: {self.__creacion}

        '''

class DetalleFactura(Factura):
    def __init__(self,city,id_type, first_name, last_name,address,phone_number, date_birth,id, iva, subtotal, total, created_at, product,price,quantity,subtotal_p ):

        super().__init__(city,id_type, first_name, last_name,address,phone_number, date_birth,id,iva,subtotal,total, created_at)
        self.__producto = product
        self.__precio = price
        self.__cantidad = quantity
        self.__subtotalP = subtotal_p

    @property
    def product(self):
        return self.__producto

    @property
    def price(self):
        return self.__precio

    @property
    def quantity(self):
        return self.__cantidad

    @property
    def subtotal_p(self):
        return self.__subtotalP

    @product.setter
    def product(self, product):
        self.__producto = product

    @price.setter
    def price(self, price):
        self.__precio = price

    @quantity.setter
    def quantity(self, quantity):
        self.__cantidad = quantity

    @subtotal_p.setter
    def subtotal_p(self, subtotal_p):
        self.__subtotalP = subtotal_p

    def __str__(self):
        return f'''
        No. {super().id}
        Cliente {super().cliente}
        Fecha de creacion {super().fecha}
        Producto: {self.__producto}
        Cantidad: {self.__cantidad}
        Precio: {self.__precio}
        Subtotal: {self.__subtotalP}

        Subtotal de la factura: {super().subtotal}
        Total de la factura: {super().total}


        '''