from models import session, Salon, Customer, Appointment

if __name__ == '__main__':
    salon = session.query(Salon).first()
    customer = session.query(Customer).first()
    appointment = session.query(Appointment).first()

    import ipdb
    ipdb.set_trace()
