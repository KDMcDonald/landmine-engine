class State:

    def __init__(self, value):
        self.value = value

class BooleanState(State):
    def __init__(self, value : bool):
        super().__init__(value=value)