from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from faker.exceptions import UniquenessException
import random
from models import Salon, Customer, Service, Appointment

DATABASE_URL = 'sqlite:///salon.db'

fake = Faker()


def create_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def seed_data():
    print("seeding data...")

    session = create_session()

    session.query(Salon).delete()
    session.query(Customer).delete()
    session.query(Service).delete()
    session.query(Appointment).delete()

    salons = []
    for _ in range(3):
        salon_name = fake.unique.first_name() + " Salon"
        salon_location = fake.unique.address()

        salon = Salon(name=salon_name, location=salon_location)
        salons.append(salon)
        session.add(salon)
    session.commit()

    customers = []
    for _ in range(5):
        customer_name = fake.unique.name()

        customer = Customer(name=customer_name)
        customers.append(customer)
        session.add(customer)
    session.commit()

    services = []
    salon_services = [
        "Haircut and Styling", "Hair Coloring and Highlights",
        "Manicure and Pedicure", "Facials and Skin Care Treatments",
        "Waxing and Hair Removal", "Massage Therapy",
        "Eyebrow and Eyelash Services", "Hair Extensions",
        "Bridal and Special Occasion Styling", "Makeup Application"
    ]
    for salon_service in salon_services:
        service_name = salon_service
        # Sevice price
        whole_part = fake.random_int(min=1, max=1000)
        decimal_part = fake.random_int(min=0, max=99)
        service_price = float(f"{whole_part}.{decimal_part:02d}")
        # Salon id
        salon_id = random.choice(salons).id

        service = Service(name=service_name,
                          price=service_price,
                          salon_id=salon_id)
        services.append(service)
    session.add_all(services)
    session.commit()

    appointments = []
    for _ in range(10):
        customer_id = random.choice(customers).id
        service_id = random.choice(services).id
        appointment_time = fake.date_time_this_year().replace(microsecond=0)

        appointment = Appointment(customer_id=customer_id,
                                  service_id=service_id,
                                  appointment_time=appointment_time)
        appointments.append(appointment)
    session.add_all(appointments)
    session.commit()

    print("seeding complete!")


if __name__ == '__main__':
    seed_data()
