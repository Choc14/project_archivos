import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

###-- BASE DE DATOS POR DEFECTO, USO DE PRUEBA --### 
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

### -- CONFIGURACION PARA LOS DIFERENTES MOTORES DE BASE DE DATOS--##

#POSTGRES
__nameBasePOST=''
__userPOST=''
__passwordPOST=''

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': __nameBasePOST,
        'USER': __userPOST,
        'PASSWORD': __passwordPOST,
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

#MYSQL
__nameDBMysql=''
__userMyS=''
__passwordMyS=''
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': __nameDBMysql,
        'USER': __userMyS,
        'PASSWORD': __passwordMyS,
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}