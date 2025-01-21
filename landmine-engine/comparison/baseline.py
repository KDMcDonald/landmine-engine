from state import State, BooleanState

class Baseline:
    
    def __init__(self, name : str, expected_state : State):
        self.name = name
        self.expected_state = expected_state