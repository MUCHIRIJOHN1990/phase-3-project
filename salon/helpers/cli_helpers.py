from services import SalonService, CustomerService, ServiceService
from models import session


def exit_program():
    print("Goodbye")
    exit()


def list_all_salons():
    salons = SalonService(session).get_all_salons()
    if salons:
        for salon in salons:
            print(salon)
    else:
        print("No salons available. Add one to view it here.")


def list_salon_by_id():
    from helpers import validate_int
    salon_id = input("Enter salon id: ")
    try:
        validate_int(salon_id)
        print(SalonService(session).get_salon_by_id(salon_id))
    except Exception as e:
        print(e)


def add_new_salon():
    try:
        name = input("Enter new salon name: ")
        location = input("Enter new salon location: ")
        print(SalonService(session).create_salon(name, location))
    except Exception as e:
        print(e)


def update_salon_location():
    from helpers import validate_int
    try:
        salon_id = input("Enter salon id: ")
        validate_int(salon_id)
        new_location = input("Enter new location: ")
        print(
            SalonService(session).update_salon_location(
                salon_id, new_location))
    except Exception as e:
        print(e)


def remove_salon():
    from helpers import validate_int
    try:
        salon_id = input("Enter salon id: ")
        validate_int(salon_id)
        SalonService(session).delete_salon(salon_id)
        print(f"Success: Salon with id {salon_id} deleted!")
    except Exception as e:
        print(e)


def list_all_customers():
    for customer in CustomerService(session).get_all_customers():
        print(customer)


def list_customer_by_id():
    from helpers import validate_int
    try:
        customer_id = input("Enter customer id: ")
        validate_int(customer_id)
        print(CustomerService(session).get_customer_by_id(customer_id))
    except Exception as e:
        print(e)


def add_new_customer():
    try:
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        print(CustomerService(session).create_customer(name=name, phone=phone))
    except Exception as e:
        print(e)


def update_customer_phone_number():
    from helpers import validate_int
    try:
        customer_id = input("Enter customer id: ")
        new_phone_number = input("Enter new phone number: ")
        validate_int(customer_id)
        print(
            CustomerService(session).update_customer_phone_number(
                customer_id=customer_id, new_phone_number=new_phone_number))
    except Exception as e:
        print(e)


def remove_customer():
    from helpers import validate_int
    try:
        customer_id = input("Enter customer id: ")
        validate_int(customer_id)
        CustomerService(session).delete_customer(customer_id=customer_id)
        print(f"Success: Customer with id {customer_id} deleted!")
    except Exception as e:
        print(e)


def list_all_services():
    services = ServiceService(session).get_all_services()

    if services:
        for service in services:
            print(service)
    else:
        print("No services available. Add one to view it here.")


def list_service_by_id():
    from helpers import validate_int
    try:
        service_id = input("Enter service id: ")
        validate_int(service_id)
        print(ServiceService(session).get_service_by_id(service_id=service_id))
    except Exception as e:
        print(e)


def add_service():
    from helpers import validate_price, validate_int
    try:
        service_name = input("Enter service name: ")
        service_price = input("Enter service price: ")
        validate_price(service_price)
        salon_id = input("Enter the salon id of the new service: ")
        validate_int(salon_id)

        print(
            ServiceService(session).create_service(service_name=service_name,
                                                   service_price=service_price,
                                                   salon_id=salon_id))
    except Exception as e:
        print(e)


def update_service_price():
    from helpers import validate_price, validate_int
    try:
        service_id = input("Enter service id: ")
        validate_int(service_id)
        new_price = input("Enter new price: ")
        validate_price(new_price)

        ServiceService(session).update_service_price(service_id=service_id,
                                                     new_price=new_price)
        print(f"Success: Price of service {service_id} updated!")
    except Exception as e:
        print(e)
