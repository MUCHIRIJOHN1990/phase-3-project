from models import Salon


class SalonService:

    def __init__(self, session):
        self.session = session

    def create_salon(self, name, location):
        """Create a new salon with the given name and location.

        Args:
            name: The name of the salon to create.
            location: The location of the salon to create.

        Returns:
            The newly created salon.
        """

        existing_salon = self.session.query(Salon).filter_by(
            name=name, location=location).first()

        if existing_salon:
            raise ValueError("Error: Salon already exists!")

        salon = Salon(name=name, location=location)
        self.session.add(salon)
        self.session.commit()

        return salon

    def get_all_salons(self):
        """Returns a list of all salons"""
        return self.session.query(Salon).all()

    def get_salon_by_id(self, salon_id):
        """Retrieves a salon by its ID.

        Args:
            salon_id: The ID of the salon to retrieve.

        Returns:
            The requested salon.

        Raises:
            EntityNotFoundException: The salon with the given ID does not exist.
        """
        salon = self.session.query(Salon).get(salon_id)
        if salon is None:
            raise ValueError(f"Error: Salon with id {salon_id} not found!")
        return salon

    def update_salon_name(self, salon_id, new_name):
        """Updates a salon's name.

        Args:
            salon_id: The ID of the salon to update.
            new_name: The new name of the salon.

        Returns:
            The updated salon.
        """
        salon = self.get_salon_by_id(salon_id)
        salon.name = new_name
        self.session.commit()
        return salon

    def update_salon_location(self, salon_id, new_location):
        """Updates a salon's location.

        Args:
            salon_id: The ID of the salon to update.
            new_location: The new location of the salon.

        Returns:
            The updated salon.
        """
        salon = self.get_salon_by_id(salon_id)
        salon.location = new_location
        self.session.commit()
        return salon

    def delete_salon(self, salon_id):
        """Deletes a salon and cascades to services if applicable.

        Args:
            salon_id: The ID of the salon to delete.
        """
        salon = self.get_salon_by_id(salon_id)
        self.session.delete(salon)
        self.session.commit()
