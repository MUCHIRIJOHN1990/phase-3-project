## Salon Management System - A Python Application

This project provides a basic salon management system written in Python. It allows you to manage salons, customers, services, and appointments.

### Installation

1. **Prerequisites:**
    * Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * Pipenv (install using `pip install pipenv`)
2. **Clone or download the repository**
    ```bash
    git clone https://github.com/MUCHIRIJOHN1990/phase-3-project.git
    cd phase-3-project
    ```
3. **Create and activate a virtual environment:**
    ```bash
    pipenv shell
    ```
4. **Install dependencies:**
    ```bash
    pipenv install
    ```

### Usage

1. **Run the application:**
    ```bash
    python salon/cli.py
    ```

2. **Interact with the application using the provided methods in the `salon/services` directory:**

    * `salon_service.py`: Manage salons (create, read, update, delete)
    * `customer_service.py`: Manage customers (create, read, update, delete)
    * `service_service.py`: Manage services (create, read, update, delete)
    * `appointment_service.py`: Manage appointments (create, read, update, delete)


### Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or new features. 

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.
