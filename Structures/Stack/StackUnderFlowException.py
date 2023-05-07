class StackUnderFlowException(Exception):
    def __init__(self):
        raise Exception("Can't remove from empty stack")