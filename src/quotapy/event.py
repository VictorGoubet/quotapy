import uuid
import typing

class Event():
    """Represent a client instance
    """
    
    def __init__(self, name:str) -> None:
        """Initialize a client

        :param str name: The name of the client
        """
        self.name = name
        self.__actions = {}
        self.__triggers = {}
        self.id = uuid.uuid4()
        
        
    def __str__(self) -> str:
        repr = f"{self.name}"
        return repr
    
    
    def add_action(self, action:typing.Callable) -> str:
        """Add an action to perform when the event is triggered

        :param typing.Callable action: The action to add
        :return str: The id of the action
        """
        action_id = uuid.uuid4()
        self.__actions[action_id] = action
    
    
    def remove_action(self, action_id:str) -> None:
        """Remove an action

        :param str action_id: The id of the action to remove
        """
        if action_id not in self.__actions:
            raise Exception(f"The action id {action_id} is not in the current actions")
        else:
            self.__actions.pop(action_id)
            
            
    def add_trigger(self, trigger:typing.Callable) -> str:
        """Add a trigger which must return a bool value and will allow to launch the actions

        :param typing.Callable trigger: The trigger to add
        :return str: The id of the trigger
        """
        trigger_id = uuid.uuid4()
        self.__triggers[trigger_id] = trigger
    
    
    def remove_trigger(self, trigger_id:str) -> None:
        """Remove an action

        :param str action_id: The id of the action to remove
        """
        if trigger_id not in self.__triggers:
            raise Exception(f"The trigger id {trigger_id} is not in the current triggers")
        else:
            self.__triggers.pop(trigger_id)
            
            
    def excute_triggers(self) -> None:
        """Execute each trigger
        """
        for trigger_id, trigger in self.__triggers.items():
            try:
                res = trigger()
                if isinstance(res, bool) and res:
                    self.execute_actions()
            except Exception as e:
                print(f"Got an exception during the execution of trigger {trigger_id}")
    
    
    def execute_actions(self) -> None:
        """Execute all the action
        """
        for action_id, action in self.__actions.items():
            try:
                action()
            except Exception as e:
                print(f"Got an exception during the execution of action {action_id}")