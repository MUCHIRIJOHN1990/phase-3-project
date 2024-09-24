from services import SalonService
from models import session


def exit_program():
    print("Goodbye")
    exit()


def list_all_salons():
    for salon in SalonService(session).get_all_salons():
        print(salon)


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
