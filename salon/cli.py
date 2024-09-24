from helpers import (exit_program, list_all_salons, list_salon_by_id,
                     add_new_salon, update_salon_location, remove_salon,
                     list_all_customers, list_customer_by_id, add_new_customer,
                     update_customer_phone_number, remove_customer,
                     list_all_services, list_service_by_id, add_service,
                     update_service_price, remove_service,
                     list_all_appointments, list_appointments_by_customer,
                     list_appointments_by_service, book_appointment,
                     delete_appointment)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == '0':
            exit_program()
        if choice == '1':
            list_all_salons()
        if choice == '2':
            list_salon_by_id()
        if choice == '3':
            add_new_salon()
        if choice == '4':
            update_salon_location()
        if choice == '5':
            remove_salon()
        if choice == '6':
            list_all_customers()
        if choice == '7':
            list_customer_by_id()
        if choice == '8':
            add_new_customer()
        if choice == '9':
            update_customer_phone_number()
        if choice == '10':
            remove_customer()
        if choice == '11':
            list_all_services()
        if choice == '12':
            list_service_by_id()
        if choice == '13':
            add_service()
        if choice == '14':
            update_service_price()
        if choice == '15':
            remove_service()
        if choice == '16':
            list_all_appointments()
        if choice == '17':
            list_appointments_by_customer()
        if choice == '18':
            list_appointments_by_service()
        if choice == '19':
            book_appointment()
        if choice == '20':
            delete_appointment()


def menu():
    print(
        "============================================================================"
    )
    print("Please select an option:")
    print("0. Exit the program")
    print("-----Salon-----")
    print("1. List all salons")
    print("2. List salon by id")
    print("3. Add new salon")
    print("4. Update salon location")
    print("5. Remove salon")
    print("-----Customer-----")
    print("6. List all customers")
    print("7. List customer by id")
    print("8. Add new customer")
    print("9. Update customer phone number")
    print("10. Remove customer")
    print("-----Service-----")
    print("11. List all services")
    print("12. List service by id")
    print("13. Add service")
    print("14. Update service price")
    print("15. Remove service")
    print("-----Appointments-----")
    print("16. List all appointments")
    print("17. List appointments by customer")
    print("18. List appointments by service")
    print("19. Book an appointment")
    print("20. Cancel appointment")
    print(
        "============================================================================"
    )


if __name__ == '__main__':
    main()
