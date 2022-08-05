# PARA ELIMINAR LAS BASES DE DATOS

rutas = [
            'apps/products/migrations/0001_initial.py',        
            'apps/customers/migrations/0001_initial.py',
            'apps/users/migrations/0001_initial.py',
            'db.sqlite3',
            ]

rutas1 = [
    'manage.py dumpdata products.Category --format=json --indent=4 > apps/products/fixtures/Category.json',
    'manage.py dumpdata products.Product --format=json --indent=4 > apps/products/fixtures/Product.json',

    'manage.py dumpdata customers.City --format=json --indent=4 > apps/customers/fixtures/City.json',
    'manage.py dumpdata customers.Id --format=json --indent=4 > apps/customers/fixtures/Id.json',
    'manage.py dumpdata customers.Customer --format=json --indent=4 > apps/customers/fixtures/Customer.json',

    'manage.py dumpdata users.User --format=json --indent=4 > apps/users/fixtures/User.json',
]

rutas2 = [
    'manage.py loaddata Category.json',
    'manage.py loaddata Product.json',

    'manage.py loaddata City.json',
    'manage.py loaddata Id.json',
    'manage.py loaddata Customer.json',

    'manage.py loaddata User.json',

]