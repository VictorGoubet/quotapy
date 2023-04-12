import uuid


class Client():
    """Represent a client instance
    """
    
    def __init__(self, name:str) -> None:
        """Initialize a client

        :param str name: The name of the client
        """
        self.name = name
        self.id = uuid.uuid4()
        
        
    def __str__(self) -> str:
        repr = f"{self.name}"
        return repr