from models import Service


class ServiceService:

    def __init__(self, session):
        self.session = session

    def create_service(self, service_name, service_price, salon_id):
        """Creates a service in the given salon.

        Args:
          name: The name of the service
          price: The price of the service
          salon_id: The ID of the salon the service belongs to

        Returns:
          Service: The newly created service
        """

        existing_service = self.session.query(Service).filter_by(
            name=service_name, salon_id=salon_id).first()
        if existing_service:
            raise ValueError("Error: Service already exists!")

        new_service = Service(name=service_name,
                              price=service_price,
                              salon_id=salon_id)
        self.session.add(new_service)
        self.session.commit()
        return new_service

    def get_all_services(self):
        """Returns all services."""

        return self.session.query(Service).all()

    def get_service_by_id(self, service_id):
        """Retrieves a service by its ID.

        Args:
          service_id: The ID of the service

        Raises EntityNotFoundException if the given service doesn't exist.
        """
        if service := self.session.query(Service).get(service_id):
            return service
        else:
            raise ValueError(f"Error: Service with id {service_id} not found!")

    def get_services_by_salon(self, salon_id):
        """Returns all services in the given salon.

        Args:
          salon_id: The ID of the salon

        Raises EntityNotFoundException if the given salon doesn't exist.
        """
        from . import SalonService
        SalonService(self.session).get_salon_by_id(salon_id)
        return self.session.query(Service).filter_by(salon_id=salon_id)

    def update_service_price(self, service_id, new_price):
        """Updates a service's price in the given salon.

        Args:
            service_id: The ID of the service to update.
            new_price: The new price of the service.

        Raises EntityNotFoundException if the given service doesn't exist.
        """
        service = self.get_service_by_id(service_id)
        service.price = new_price
        self.session.commit()

    def delete_service(self, service_id):
        """Deletes a service and cascades to appointments.

        Args:
          service_id: The ID of the service to delete

        Raises EntityNotFoundException if the given service doesn't exist.
        """
        service = self.get_service_by_id(service_id)
        self.session.delete(service)
        self.session.commit()
