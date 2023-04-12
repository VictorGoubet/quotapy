import uuid


class QuotasTable():
    """Represent an instance of a quotas table
    """
    
    def __init__(self, name:str) -> None:
        """Initialize a quotas table

        :param str name: The name of the table
        """
        self.name = name
        self.id = uuid.uuid4()
        self.usecases = {}
        self.client = {}
        self.event = {}
        self.table = []

    
    
    
    def __str__(self) -> str:
        repr = f"{self.name}"
        return repr