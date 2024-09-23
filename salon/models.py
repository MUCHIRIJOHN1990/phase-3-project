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

    def __repr__(self):
        return f"Salon(name={self.name}, location={self.location})"


# Cusotmer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)

    services = relationship('Service',
                            secondary=customers_services,
                            back_populates='customers')
    appointments = relationship('Appointment', backref='customer')

    def __repr__(self):
        return f"Customer(name={self.name})"


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

    def __repr__(self):
        return f"Service(name={self.name}, price={self.price}, salon_id={self.salon_id})"


# Appointment model
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    service = Column(Integer, ForeignKey('services.id'))

    def __repr__(self):
        return f"Appointment(created_at={self.created_at}, customer-id={self.customer_id}, service={self.service})"
