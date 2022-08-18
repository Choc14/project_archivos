class Usuarios:
    def __init__(self, first_name = None, last_name = None, username = None, password = None, user_type = 'Usuario', email = None):
        self.__nombre = first_name
        self.__apellido = last_name
        self.__username = username
        self.__password = password
        self.__tipo_usuario = user_type
        self.__correo = email

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @property
    def correo(self):
        return self.__correo

    @nombre.setter
    def nombre(self, first_name):
        self.__nombre = first_name

    @apellido.setter
    def apellido(self, last_name):
        self.__apellido = last_name

    @username.setter
    def username(self, username):
        self.__username = username

    @password.setter
    def password(self, password):
        self.__password = password

    @tipo_usuario.setter
    def tipo_usuario(self, user_type):
        self.__tipo_usuario = user_type

    @correo.setter
    def correo(self, email):
        self.__correo = email

    def __str__(self):
        return f'''
        Nombre del usuario: {self.__nombre} 
        Apellido del usuario: {self.__apellido}
        Nombre de usuario: {self.__username}
        Tipo de usuario: {self.__tipo_usuario}
        Correo: {self.__correo}
        '''