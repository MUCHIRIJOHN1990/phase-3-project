from services import SalonService, CustomerService, ServiceService, AppointmentService
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


def remove_service():
    from helpers import validate_int
    try:
        service_id = input("Enter service id: ")
        validate_int(service_id)
        ServiceService(session).delete_service(service_id=service_id)
        print(f"Success: Service with id {service_id} deleted!")
    except Exception as e:
        print(e)


def list_all_appointments():
    for appointment in AppointmentService(session).get_all__apointments():
        print(appointment)


def list_appointments_by_customer():
    from helpers import validate_int
    try:
        customer_id = input("Enter customer id: ")
        validate_int(customer_id)
        customer = CustomerService(session).get_customer_by_id(customer_id)
        if appointments := customer.appointments:
            for appointment in appointments:
                print(appointment)
        else:
            print(
                f"No existing appointments for customer with id {customer_id}")
    except Exception as e:
        print(e)


def list_appointments_by_service():
    from helpers import validate_int
    try:
        service_id = input("Enter service id: ")
        validate_int(service_id)
        service = ServiceService(session).get_service_by_id(service_id)
        if services := service.appointments:
            for service in services:
                print(service)
        else:
            print(f"No existing appointments for service with id {service_id}")
    except Exception as e:
        print(e)


def book_appointment():
    from datetime import datetime
    from helpers import validate_int
    try:
        current_date = datetime.now()
        default_year = current_date.year
        default_month = current_date.month
        default_day = current_date.day
        default_hour = current_date.hour

        customer_id = input(
            "Enter the id of the customer, you would like to create and appointment for: "
        )
        CustomerService(session).get_customer_by_id(customer_id=customer_id)
        validate_int(customer_id)
        service_id = input(
            "Enter the service id you wish to create an appointment for: ")
        validate_int(service_id)
        ServiceService(session).get_service_by_id(service_id=service_id)
        year = input("Enter the year (optional, defaults to current year): ")
        if not year:
            year = default_year
        validate_int(year)
        month = input(
            "Enter the month (optional, defaults to current month): ")
        if not month:
            month = default_month
        validate_int(month)
        day = input("Enter the day, (optional, defaults to current day): ")
        if not day:
            day = default_day
        validate_int(day)
        hour = input(
            "Enter the hour (optional, defaults to current hour) (in 24-hour format): "
        )
        if not hour:
            hour = default_hour
        minute = input("Enter the minute (optional defaults to 00): ")
        if not minute:
            minute = 0

        date_time = datetime(year, month, day, hour, minute)

        print(
            AppointmentService(session).create_appointment(
                customer_id=customer_id,
                time_slot=date_time,
                service_id=service_id))
    except Exception as e:
        print(e)


def delete_appointment():
    from helpers import validate_int

    try:
        appointment_id = validate_int(input("Enter appointmentmed id: "))
        AppointmentService(session).delete_appointment(
            appointment_id=appointment_id)
        print(f"Success: deleted appointment with id {appointment_id}")
    except Exception as e:
        print(e)
