from models import Customer


class CustomerService:

    def __init__(self, session):
        self.session = session

    def create_customer(self, name, phone):
        """Creates a new Customer with the given name and phone number.

        Args:
            name: The name of the customer.
            phone: The phone number of the customer.

        Returns:
            Customer: The newly created customer.
        """
        existing_customer = self.session.query(Customer).filter_by(
            name=name, phone=phone).first()
        if existing_customer:
            raise ValueError("Error: Customer already exists!")

        new_customer = Customer(name=name, phone=phone)
        self.session.add(new_customer)
        self.session.commit()
        return new_customer

    def get_all_customers(self):
        """Retrieves all customers"""
        return self.session.query(Customer).all()

    def get_customer_by_id(self, customer_id: int) -> Customer:
        """Retrieves a customer by ID.

        Args:
            customer_id: The ID of the customer.

        Returns:
            Customer: The customer associated with the given ID.

        Raises:
            EntityNotFoundException: The customer with the given ID does not exist.
        """
        customer = self.session.query(Customer).get(customer_id)
        if customer is None:
            raise ValueError(
                f"Error: Customer with id {customer_id} not found!")
        return customer

    def get_customer_by_name(self, name):
        """Retrieves a customer by name.

        Args:
            name: The name of the customer to retrieve.

        Returns:
            Customer: The customer associated with the given name.

        Raises:
            EntityNotFoundException: The customer with the given name does not exist.
        """
        customer = self.session.query(Customer).filter_by(name=name).first()
        if customer is None:
            raise ValueError(f"Error: Customer with name {name} not found!")
        return customer

    def update_customer_phone_number(self, customer_id, new_phone_number):
        """Updates a customer's phone number.

        Args:
            customer_id: The ID of the customer to update.
            new_phone: The new phone number of the customer.

        Returns:
            Customer: The updated customer.
        """
        customer = self.get_customer_by_id(customer_id)
        customer.phone = new_phone_number
        self.session.commit()
        return customer

    def update_customer_name(self, customer_id, new_name):
        """Updates a customer's name.

        Args:
            customer_id: The ID of the customer to update.
            new_name: The new name of the customer.

        Returns:
            Customer: The customer with the updated name.
        """
        customer = self.get_customer_by_id(customer_id)
        customer.name = new_name
        self.session.commit()
        return customer

    def delete_customer(self, customer_id):
        """Deletes a customer and cascades to their appointments.

        Args:
            customer_id: The ID of the customer to delete.
        """
        customer = self.get_customer_by_id(customer_id)
        self.session.delete(customer)
        self.session.commit()
