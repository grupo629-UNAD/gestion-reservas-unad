# se importan las clases de los módulos Services, Customer y Order para utilizarlas en el código
from models.Customer import Customer
from models.catalog import ServiceCatalog
from models.Order import Order 

# se importan las funciones de validación y el gestor de logs para utilizarlos en el código
from utils.validadores import (
    validate_email,
    validate_not_empty,
    validate_only_numbers
)
from utils.gestor_logs import log_error_message

# se definen listas globales para simular el almacenamiento de datos en memoria durante la ejecución
customer_list = [] 
order_list = []
catalog = ServiceCatalog() 

# se define una función para registrar un nuevo cliente con validaciones estrictas y manejo de excepciones
def register_customer():
    print("\n--- Customer Registration ---")
    while True:
        try:
            name = input("Full Name: ")
            validate_not_empty(name, "Name")

            email = input("Email: ")
            validate_email(email)

            phone = input("Phone: ")
            validate_only_numbers(phone, "Phone")

            address = input("Address: ")
            validate_not_empty(address, "Address")

            # se genera un ID automático y se crea la instancia de Customer usando atributos encapsulados
            new_id = f"C{len(customer_list)+1:03d}"
            new_customer = Customer(new_id, name, email, phone, address)
            
            return new_customer
    
        except ValueError as error:
            # se captura el error de validación, se muestra al usuario y se registra en el archivo de logs
            print(f"\n[!] Input Error: {error}")
            log_error_message(f"Registration Error: {error}")
            print("Please try again.\n")

# se define una función para crear una reserva, vinculando un cliente existente con un servicio del catálogo
def create_order():
    if not customer_list:
        print("\n[!] Error: No customers registered yet.")
        return

    print("\n--- Create New Reservation ---")
    c_id = input("Enter Customer ID (e.g., C001): ")
    
    # se busca al cliente en la lista global utilizando su ID de sistema
    customer = next((c for c in customer_list if c.id_system == c_id), None)
    
    if not customer:
        print("Customer not found.")
        log_error_message(f"Order Error: Customer ID {c_id} not found.")
        return

    print("\n--- Available Services ---")
    for s in catalog.services:
        print(s.get_info())
    
    service_id = input("\nEnter the ID of the service to hire: ")
    selected_service = catalog.search_service(service_id)
    
    if selected_service:
        try:
            # se solicita el descuento para demostrar la sobrecarga de métodos y el polimorfismo
            disc = input("Enter discount % (0 for none): ")
            validate_only_numbers(disc, "Discount")
            
            # se crea el pedido y se agrega el servicio con el cálculo de costo polimórfico
            new_order = Order(id_system=f"O{len(order_list)+1:03d}", customer_id=customer.id_system)
            
            # se aplica el descuento opcional al servicio antes de mostrar el total
            final_cost = selected_service.calculate_cost(discount=float(disc))
            new_order.add_service(selected_service)
            order_list.append(new_order)
            
            print(f"\n[SUCCESS] Order created for {customer.name}!")
            print(f"Total with discount: ${final_cost}")
            
        except ValueError as ve:
            print(f"[!] Invalid input: {ve}")
            log_error_message(f"Order Creation Error: {ve}")
    else:
        print("Service not found.")
        log_error_message(f"Order Error: Service ID {service_id} not found.")

# se define la función principal que mantiene el programa en ejecución mediante un menú interactivo
def main_menu():
    while True:
        print("\n================================")
        print("   SOFTWARE FJ MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register Customer")
        print("2. Create Reservation")
        print("3. View Registered Customers")
        print("4. Exit")
        
        option = input("\nSelect an option (1-4): ")
        
        if option == "1":
            new_client = register_customer()
            customer_list.append(new_client)
            print(f"\nCustomer {new_client.name} registered successfully!")
            
        elif option == "2":
            create_order()
            
        elif option == "3":
            print("\n--- Registered Customers List ---")
            for c in customer_list:
                print(c.get_info())
                
        elif option == "4":
            print("Closing system. Thank you for using Software FJ.")
            break
        else:
            print("Invalid option, please try again.")

# punto de entrada principal del programa que inicia el bucle del menú
if __name__ == "__main__":
    main_menu()