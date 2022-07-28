# PROYECTO FASE 1 DE MANEJO DE ARCHIVOS

## MIEMBROS

- DIEGO ALEJANDRO MORALES
- EVER CORAZON
- JUAN CARLOS CHOC XOL

## Instalacion 

- Creacion del entorno virtual
- Activar el entorno virtual
- Clonar el repositorio
- Instalar los paquetes

> Los siguientes comandos se deben de ejecutar desde la terminal cmd

## _Creacion del Entorno virtual_
```sh
python -m venv venv


```
## _Activar el Entorno virtual_
```sh
venv\scripts\activate

```

> PARA DESACTIVAR EL ENTORNO VIRTUAL
## Desactivar el Entorno virtual_
```sh
deactivate

```

## _Clonar el repositorio_
```sh
git clone direccion del repositorio

```

## _Instalar los paquetes_
```sh
cd project_archivos
python -m pip install -r requirements.txt

> Si instala nuevas librerias o dependencias ejecutar el siguiente comando
pip freeze > requirements.txt
```


## Creacion de aplicaciones
```sh
cd apps
django-admin startapp nombre_de_la_aplicacion

```