# se importa la clase base EntidadBase y las clases de servicios Consulting, EquipmentRental y RoomReservation para definir la estructura del catálogo de servicios
from models.Services import Consulting, EquipmentRental, RoomReservation

# se define la clase ServiceCatalog para gestionar el catálogo de servicios disponibles, con una lista de servicios y métodos para agregar servicios al catálogo
class ServiceCatalog:
    def __init__(self):
        self.services = [] # se define una lista para almacenar los servicios disponibles en el catálogo
        self.load_default_services() # se carga el catálogo con servicios predeterminados al crear una instancia de ServiceCatalog  
        
    # se define un método para agregar un servicio al catálogo
    def add_service_to_catalog(self, service):
        self.services.append(service)

    # se define un método para cargar servicios predeterminados en el catálogo, que agrega una serie de servicios de consultoría, salas y equipos tecnológicos al catálogo utilizando el método add_service_to_catalog
    def load_default_services(self):
        # 3 Consultas Tecnológicas (ID, Name, Price, Hours)
        self.add_service_to_catalog(Consulting("C001", "Cloud Infrastructure Audit", 500.0, 1.0))
        self.add_service_to_catalog(Consulting("C002", "Cybersecurity Strategy Plan", 450.0, 1.0))
        self.add_service_to_catalog(Consulting("C003", "Software Architecture Review", 300.0, 1.0))
        
        # 3 Salas (ID, Name, Price_per_hour, Hours)
        self.add_service_to_catalog(RoomReservation("R001", "Dev Sprint Meeting Room", 120.0, 1.0))
        self.add_service_to_catalog(RoomReservation("R002", "Remote Collaboration Hub", 150.0, 1.0))
        self.add_service_to_catalog(RoomReservation("R003", "Server Room Access", 100.0, 1.0))
        
        # 3 Equipos (ID, Name, Price_per_day, Days)
        self.add_service_to_catalog(EquipmentRental("E001", "High-Performance Laptop", 300.0, 1.0))
        self.add_service_to_catalog(EquipmentRental("E002", "VR Development Headset", 200.0, 1.0))
        self.add_service_to_catalog(EquipmentRental("E003", "Network Testing Device", 80.0, 1.0))

   # se define un método para buscar un servicio en el catálogo por su ID de sistema
    def search_service(self, service_id):
        # recorre la lista de servicios y devuelve el primero que coincida con el ID, o None si no existe
        return next((s for s in self.services if s.id_system == service_id), None)
    