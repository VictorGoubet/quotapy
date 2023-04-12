import uuid


class Usecase():
    """Represent a usecase instance
    """
    
    def __init__(self, name:str) -> None:
        """Initialize a usecase

        :param str name: The name of the usecase
        """
        self.name = name
        self.id = uuid.uuid4()
        
        
    def __str__(self) -> str:
        repr = f"{self.name}"
        return repr