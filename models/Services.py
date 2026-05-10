# se importa la clase base EntidadBase y las clases abstractas ABC y abstractmethod para definir la estructura de las clase Service
from models.Entidad_base import EntidadBase
from abc import ABC, abstractmethod

# se define la clase hija que hereda de EntidadBase, con un atributo adicional service
class Service(EntidadBase, ABC):
    def __init__(self, id_system, price):
        super().__init__(id_system)
        self.price = float(price)
    
    # se define un método abstracto para calcular el costo, que debe ser implementado por las clases hijas
    @abstractmethod
    def calculate_cost(self, discount=0):
        pass

    # se define un método abstracto para obtener la información, que debe ser implementado por las clases hijas
    @abstractmethod
    def get_info(self):
        pass

# se define la clase hija que hereda de Service, con un atributo adicional hours
class Consulting(Service):
    def __init__(self, id_system, name, price, hours):
        super().__init__(id_system, float(price))
        self.name = name
        self.hours = float(hours)

    # se define un método para calcular el costo del servicio de consultoría, multiplicando el precio por el número de horas, y aplicando un descuento opcional
    def calculate_cost(self, discount=0):
        total = self.price * self.hours
        return total - (total * (discount / 100))

    # se define un método para obtener la información del servicio de consultoría, devolviendo una cadena con los detalles
    def get_info(self):
        return f"ID: {self.id_system} | Service: {self.name} (Consulting) | Price/h: ${self.price} | Hours: {self.hours}"

# se define la clase hija que hereda de Service, con un atributo adicional days    
class EquipmentRental(Service):
    def __init__(self, id_system, name, price_per_day, days):
        super().__init__(id_system, float(price_per_day))
        self.name = name
        self.days = float(days)

    # se define un método para calcular el costo del servicio de alquiler de equipo, multiplicando el precio por día por el número de días, y aplicando un descuento opcional
    def calculate_cost(self, discount=0):
        total = self.price * self.days
        return total - (total * (discount / 100))

    # se define un método para obtener la información del servicio de alquiler, devolviendo una cadena con los detalles
    def get_info(self):
        return f"ID: {self.id_system} | Service: {self.name} (Rental) | Price/day: ${self.price} | Days: {self.days}"

# se define la clase hija que hereda de Service, con un atributo adicional hours
class RoomReservation(Service):
    def __init__(self, id_system, name, price_per_hour, hours):
        super().__init__(id_system, float(price_per_hour))
        self.name = name
        self.hours = float(hours)
        
    # se define un método para calcular el costo del servicio de reserva de sala, multiplicando el precio por hora por el número de horas, y aplicando un descuento opcional
    def calculate_cost(self, discount=0):
        total = self.price * self.hours
        return total - (total * (discount / 100))

    # se define un método para obtener la información del servicio de reserva de sala, devolviendo una cadena con los detalles
    def get_info(self):
        return f"ID: {self.id_system} | Service: {self.name} (Room) | Price/h: ${self.price} | Hours: {self.hours}"