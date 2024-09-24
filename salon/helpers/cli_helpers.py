from services import SalonService
from models import session


def exit_program():
    print("Goodbye")
    exit()


def list_all_salons():
    for salon in SalonService(session).get_all_salons():
        print(salon)
