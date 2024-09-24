from models import Appointment
from helpers import EntityAlreadyExistsException, EntityNotFoundException
from . import CustomerService, ServiceService


class AppointmentService:

    def __init__(self, session):
        self.session = session

    def create_appointment(self, customer_id, service_id, time_slot):
        """Books an appointment for a customer with a given service at a specific time.

        Args:
            customer_id: The ID of the customer for whom the appointment is being booked.
            service_id: The ID of the service for which the appointment is being booked.
            time_slot: The time at which the appointment is being booked.

        Returns:
            Appointment: The newly booked appointment.
        """
        CustomerService(self.session).get_customer_by_id(customer_id)
        ServiceService(self.session).get_service_by_id(service_id)

        existing_appointment = self.session.query(Appointment).filter_by(
            customer_id=customer_id,
            service_id=service_id,
            time_slot=time_slot)
        if existing_appointment:
            raise EntityAlreadyExistsException

        appointment = Appointment(customer_id=customer_id,
                                  service_id=service_id,
                                  time_slot=time_slot)
        self.session.add(appointment)
        self.session.commit()
        return appointment

    def get_all__apointments(self):
        """Returns all appointments."""

        return self.session.query(Appointment).all()

    def get_appointment_by_id(self, appointment_id):
        """Retrieves an appointment by its ID.

        Args:
            appointment_id: The ID of the appointment to retrieve.

        Returns:
            Appointment: The appointment associated with the given ID.

        Raises:
            EntityNotFoundException: The appointment with the given ID does not exist.
        """
        if appointment := self.session.query(Appointment).get(appointment_id):
            return appointment
        else:
            raise EntityNotFoundException

    def get_appointments_by_customer(self, customer_id):
        """Returns a list of all appointments for a given customer.

        Args:
            customer_id: The ID of the customer.
        """
        CustomerService(self.session).get_customer_by_id(customer_id)

        return self.session.query(Appointment).filter_by(
            customer_id=customer_id).all()

    def list_appointments_by_service(self, service_id):
        """Lists all appointments for a given service.

        Args:
            service_id: The ID of the service.

        Returns:
            list: A list of all appointments for the service.
        """

        ServiceService(self.session).get_service_by_id(service_id)

        return self.session.query(Appointment).filter_by(
            service_id=service_id).all()

    def update_appointment_time(self, appointment_id, new_time):
        """Updates the time of an appointment.

        Args:
            appointment_id: The ID of the appointment to update.
            new_time: The new time for the appointment.
        """
        appointment = self.get_appointment_by_id(appointment_id)
        appointment.time_slot = new_time
        self.session.commit()

    def delete_appointment(self, appointment_id):
        """Cancels an appointment.

        Args:
            appointment_id: The ID of the appointment to cancel.
        """
        appointment = self.get_appointment_by_id(appointment_id)
        self.session.delete(appointment)
        self.session.commit()
