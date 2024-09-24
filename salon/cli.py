from helpers import (exit_program, list_all_salons)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == '0':
            exit_program()
        if choice == '1':
            list_all_salons()


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
    print("13. Update service price")
    print("14. Delete service")
    print("-----Appointments-----")
    print("15. List all appointments")
    print("16. List appointments by customer")
    print("17. List appointments by service")
    print("18. Book an appointment")
    print("19. Cancel appointment")
    print(
        "============================================================================"
    )


if __name__ == '__main__':
    main()
