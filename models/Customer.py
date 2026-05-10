# se iporta la clase base EntidadBase y las clases abstractas ABC y abstractmethod para definir la estructura de las clase customer
from models.Entidad_base import EntidadBase

# se define la clase hija que hereda de EntidadBase, con un atributo adicional customer
class Customer(EntidadBase):
    def __init__(self, id_system, name, email, phone, address):
        super().__init__(id_system)
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    # se definen propiedades para acceder a los atributos privados name y email, que devuelven el valor de los atributos correspondientes
    @property
    def name(self):
        return self.__name
    
    # se define una propiedad para acceder al atributo privado email, que devuelve el valor del atributo correspondiente
    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    # se define un método para obtener la información del cliente, que devuelve una cadena con los detalles del cliente
    def get_info(self):
        return f"Customer ID: {self.id_system}, Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"
