###------CREACION DE LAS CLASES CORRESPONDIENTES AL MODULO CON SUS RESPECTIVAS
# VARIABLES, METODOS-----###

class Ciudad:
    def __init__(self, city):
        self.__ciudad = city
    
    @property
    def ciudad(self):
        return self.__ciudad
    
    @ciudad.setter
    def ciudad(self, city):
        self.__ciudad = city

    def __str__(self):
        return f'Ciudad: {self.__ciudad}'



class Identificador:
    def __init__(self, id_type):
        self.__identificador = id_type
    
    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, id_type):
        self.__identificador = id_type
    
    def __str__(self):
        return f'Identificador: {self.__identificador}'


class Clientes(Ciudad, Identificador):
    def __init__(self, city, id_type ,first_name , last_name, addres , phone_number, date_birth ):
        Ciudad.__init__(self, city)
        Identificador.__init__(self, id_type)
        self.__nombre = first_name
        self.__apellido = last_name
        self.__direccion = addres
        self.__telefono = phone_number
        self.__fecha_nacimiento = date_birth

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

 
    @nombre.setter
    def nombre(self, first_name):
        self.__nombre = first_name

    @apellido.setter
    def apellido(self, last_name):
        self.__apellido = last_name

    @direccion.setter
    def direccion(self, addres):
        self.__direccion = addres

    @telefono.setter
    def telefono(self, phone_number):
        self.__telefono = phone_number

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, date_birth):
        self.__fecha_nacimiento = date_birth

    def __str__(self):
        return f'''
        Nombre del cliente: {self.__nombre} 
        Apellido del cliente: {self.__apellido}
        Direccion del cliente: {self.__direccion}
        Numero de telefono: {self.__telefono}
        Fecha de nacimiento: {self.__fecha_nacimiento}
        '''