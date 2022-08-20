###------CREACION DE LAS CLASES CORRESPONDIENTES AL MODULO CON SUS RESPECTIVAS
# VARIABLES, METODOS-----###

class Categoria:
    def __init__(self, titleCategory, description = None):
        self.__titleCategory = titleCategory
        self.__description = description

     
    @property
    def titleCategory(self):
        return self.__titleCategory
    
    @property
    def description(self):
        return self.__description
    
    @titleCategory.setter
    def titleCategory(self, titleCategory):
        self.__titleCategory = titleCategory
    
    @description.setter
    def description(self, description):
        self.__description = description

    def __str__(self) :
        return f'''
        Nombre de la categoria: {self.__titleCategory}
        Descripcion: {self.__description} 
        '''

class Producto(Categoria):  
    def __init__(self, titleCategory , titleProduct, description, price):
        super().__init__(titleCategory)
        self.__title = titleProduct
        self.__description = description
        self.__price = price
  
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price
    

    @title.setter
    def title(self, titleProduct):
        self.__title = titleProduct
    
    @description.setter
    def description(self, description):
        self.__description = description
    
    @price.setter
    def price(self, price):
        self.__price = price
    
    def __str__(self):        
        return f'''
        Nombre del producto: {self.__title}
        Descripcion: {self.__description}
        Precio: {self.__price}
{super().__str__()}
        '''

