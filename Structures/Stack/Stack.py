from Structures.List.List import List
from Structures.Stack.StackUnderFlowException import StackUnderFlowException


class Stack:
    def __init__(self):
        self.__list = List()

    def push(self, data):
        self.__list.push(data)

    def pop(self):
        tmp = self.__list.pop()
        if tmp:
            return tmp
        else:
            raise StackUnderFlowException()

    def peek(self):
        return self.__list.peek()

    def is_empty(self):
        return self.__list.is_empty()

    def __str__(self):
        return str(self.__list)
