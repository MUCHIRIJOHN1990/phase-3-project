class EntityAlreadyExistsException(Exception):
    """Exception raised when attempting to create an entity that already exists."""
    pass


class EntityNotFoundException(Exception):
    """Exception raised when attempting to retrived an entity that does not exist."""
