import os



class ArchivoUsuario:
    
    ruta_archivo = 'apps/users/txt/users/usuarios.txt'

    @classmethod
    def agregar_usurio(cls, User):
        user_list = User.objects.all()

        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            for usuario in user_list:
                archivo.write(f'{usuario.id}'.center(60,'-'))
                archivo.write(f'\n')
                archivo.write(f'Nombre del usuario: {usuario.first_name}\n')
                archivo.write(f'Apellido del usuario: {usuario.last_name}\n')
                archivo.write(f'Correo Electronico: {usuario.email}\n')
                archivo.write(f'Username: {usuario.username}\n')
                archivo.write(f'Tipo de usuario: {usuario.user_type}\n')
                
                fecha = usuario.created_at.strftime('%Y-%m-%d')
                archivo.write(f'Fecha de creacion: {fecha}\n')
                archivo.write(f'\n')


    @classmethod
    def eliminar_usuario(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

    @classmethod
    def subir(cls, User):
        cls.agregar_usurio(User)
        cls.eliminar_usuario()
        cls.agregar_usurio(User)

