from sqlalchemy import (Column, Integer, String, DateTime, func, Table, Float,
                        ForeignKey, UniqueConstraint, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///salon.db"

# Create Base class, subclassed by all moddels
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Salon model
class Salon(Base):
    __tablename__ = "salons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    services = relationship("Service",
                            backref="salon",
                            cascade="all, delete-orphan")

    def __repr__(self):
        return f"Salon(name={self.name}, location={self.location})"


# Many-to-Many relationship between Customer and Service through Appointment
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    # Appointment linking to services
    appointments = relationship("Appointment",
                                backref="customer",
                                cascade="all, delete-orphan")

    def __repr__(self):
        return f"Customer(name={self.name}, phone={self.phone})"


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    salon_id = Column(Integer, ForeignKey("salons.id"))

    # Appointment linking to customers
    appointments = relationship("Appointment",
                                backref="service",
                                cascade="all, delete-orphan")

    def __repr__(self):
        return f"Service(name={self.name}, price={self.price}, salon_id={self.salon_id})"


# Association table between Customer and Service (through Appointment)
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    time_slot = Column(DateTime, default=func.now())

    __table_args__ = (UniqueConstraint("customer_id",
                                       "service_id",
                                       "time_slot",
                                       name='uq_customer_service_time'), )

    def __repr__(self):
        return f"Appointment(created_at={self.created_at}, customer-id={self.customer_id}, service={self.service}, time_slot={self.time_slot})"
