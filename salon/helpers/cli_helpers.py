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
        salon = SalonService(session).get_salon_by_id(salon_id)
        print(salon)
    except Exception as e:
        print(e)
