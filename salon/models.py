from sqlalchemy import (Column, Integer, String, DateTime, func, Table,
                        ForeignKey)
from sqlalchemy.orm import declarative_base, relationship

# Create Base class, subclassed by all moddels
Base = declarative_base()

customers_services = Table(
    'customers_services', Base.metadata,
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    Column('service_id', ForeignKey('services.id'), primary_key=True))


# Salon model
class Salon(Base):
    __tablename__ = 'salons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    services = relationship('Service', backref='salon')


# Cusotmer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)

    services = relationship('Service',
                            secondary=customers_services,
                            back_populates='customers')
    appointments = relationship('Appointment', backref='customer')


# Service model
class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    salon_id = Column(Integer, ForeignKey('salons.id'))

    customers = relationship('Customer',
                             secondary=customers_services,
                             back_populates='services')
    appointments = relationship('Appointment', backref='service')


# Appointment model
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    service = Column(Integer, ForeignKey('services.id'))
