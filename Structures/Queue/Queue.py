from Structures.List.List import List
from Structures.Stack.StackUnderFlowException import StackUnderFlowException


class Queue:
    def __init__(self):
        self.__list = List()

    def enqueue(self, data):
        self.__list.append(data)

    def dequeue(self):
        tmp = self.__list.pop()
        if tmp:
            return tmp
        else:
            raise StackUnderFlowException()

    def is_empty(self):
        return self.__list.is_empty()

    def __sizeof__(self):
        return self.__list.__sizeof__()

    def __str__(self):
        return str(self.__list)

    def __repr__(self):
        return repr(self.__list)
