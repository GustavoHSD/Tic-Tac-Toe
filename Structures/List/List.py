from Structures.List.Node import Node
from Structures.List.IndexOutOfBoundsException import IndexOutOfBoundsException


class List:
    def __init__(self, head: Node = None, tail: Node = None):
        self.__head = head
        self.__tail = tail
        self.__length = 0

    def push(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.set_next(self.__head)
            self.__head.set_prev(node)
            self.__head = node
        self.__length += 1

    def append(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.set_prev(self.__tail)
            self.__tail.set_next(node)
            self.__tail = node
        self.__length += 1

    def add(self, data, index: int):
        if index < 0 or index > self.__length:
            raise IndexOutOfBoundsException()
        elif index == 0:
            self.push(data)
        elif index == self.__length:
            self.append(data)
        elif index < self.__length/2:
            node = Node(data)
            tmp = self.__tail
            for i in range(index):
                tmp = tmp.get_prev()
            node.set_prev(tmp.get_prev())
            tmp.set_prev(node)
        else:
            node = Node(data)
            tmp = self.__head
            for i in range(index):
                tmp = tmp.get_next()
            node.set_next(tmp.get_next())
            tmp.set_next(node)
            self.__length += 1

    def pop(self):
        if self.__head is None:
            return None
        tmp = self.__head
        self.__head = self.__head.get_next()
        self.__length -= 1
        return tmp

    def remove(self, index: int):
        if index < 0 or index >= self.__length:
            raise IndexOutOfBoundsException()
        elif index == 0:
            result = self.__head
            self.__head = self.__head.get_next()
        elif index == self.__length:
            result = self.__tail
            self.__tail = self.__tail.get_prev()
            self.__tail.set_next(None)
        elif index <= self.__length/2:
            tmp = self.__head
            for i in range(index):
                tmp = tmp.get_next()
            result = tmp
            tmp = result.get_prev()
            tmp.set_next(result.get_next())
        else:
            tmp = self.__tail
            index = self.__length - index
            for i in range(index-1):
                tmp = tmp.get_prev()
            result = tmp
            tmp = result.get_prev()
            tmp.set_next(result.get_next())
        self.__length -= 1
        return result

    def peek(self):
        return self.__head.get_data()

    def get(self, index):
        if index < 0 or index >= self.__length:
            raise IndexOutOfBoundsException()
        elif index == 0:
            tmp = self.peek()
        elif index == self.__length-1:
            tmp = self.__tail
        elif index < self.__length / 2:
            tmp = self.__head
            for i in range(index - 1):
                tmp = tmp.get_next()
        else:
            tmp = self.__tail
            index = self.__length - index
            for i in range(index - 1):
                tmp = tmp.get_prev()
        return tmp

    def is_empty(self):
        return self.__sizeof__() == 0

    def __copy__(self):
        new_list = List()
        for data in self.__data:
            new_list.push(data)
        return new_list

    def __iter__(self):
        tmp = self.__head
        while tmp:
            yield tmp.get_data()
            tmp = tmp.get_next()

    def __sizeof__(self):
        return self.__length

    def __str__(self):
        tmp = self.__head
        result = '[' if not self.is_empty() else '[]'
        while tmp is not None:
            result += f'{tmp}, ' if tmp.get_next() is not None else f'{tmp}]'
            tmp = tmp.get_next()
        return result

    def __repr__(self):
        return f'List(head={self.__head}, tail={self.__tail}, length={self.__length})'
