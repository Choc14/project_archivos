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
__nameDBMysql='pventas'
__userMyS='root'
__passwordMyS='admin'
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

#SQL SERVER
__nameDBSqlServer='pventas'
__userSqlServer='sa'
__passwordSqlServer='choc'
#DESKTOP-Q9MVAP4
SQLSERVER = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': __nameDBSqlServer,
        'USER': __userSqlServer,
        'PASSWORD': __passwordSqlServer,
        'HOST': 'DESKTOP-Q9MVAP4',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
        
    }
}