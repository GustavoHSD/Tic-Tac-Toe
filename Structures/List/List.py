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
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__length += 1

    def append(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__length += 1

    def add(self, data, index: int):
        if index < 0 or index > self.__length:
            raise IndexOutOfBoundsException(index)
        elif index == 0:
            self.push(data)
        elif index == self.__length:
            self.append(data)
        elif index < self.__length / 2:
            node = Node(data)
            tmp = self.__tail
            for i in range(index):
                tmp = tmp.prev()
            node.prev = tmp.prev
            tmp.prev = node
        else:
            node = Node(data)
            tmp = self.__head
            for i in range(index):
                tmp = tmp.next
            node.next = tmp.next
            tmp.next = node
            self.__length += 1

    def pop(self):
        if self.__head is None:
            return None
        tmp = self.__head
        self.__head = self.__head.next
        self.__length -= 1
        return tmp

    def remove(self, index: int):
        if index < 0 or index >= self.__length:
            raise IndexOutOfBoundsException(index)
        elif index == 0:
            result = self.__head
            self.__head = self.__head.next
        elif index == self.__length:
            result = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = None
        elif index <= self.__length / 2:
            tmp = self.__head
            for i in range(index):
                tmp = tmp.next
            result = tmp
            tmp = result.prev
            tmp.next = result.next
        else:
            tmp = self.__tail
            index = self.__length - index
            for i in range(index - 1):
                tmp = tmp.prev
            result = tmp
            tmp = result.prev
            tmp.next = result.next
        self.__length -= 1
        return result

    def peek(self):
        return self.__head

    def get(self, index):
        tmp = self.__head
        if index < 0 or index > self.__length - 1:
            raise IndexOutOfBoundsException(index)
        elif index == 0:
            tmp = self.__head
        elif index == self.__length - 1:
            tmp = self.__tail
        else:
            for i in range(index):
                tmp = tmp.next
        return tmp.data

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
            yield tmp.data
            tmp = tmp.next

    def __contains__(self, value):
        tmp = self.__head
        while tmp is not None:
            if tmp.data == value:
                return True
            tmp = tmp.next
        return False

    def __len__(self):
        return self.__length

    def __str__(self):
        tmp = self.__head
        result = f'[{self.__head}'
        while tmp is not None:
            tmp = tmp.next
            result += f', {tmp}' if tmp is not None else ']'
        return result

    def __repr__(self):
        return f'List(head={self.__head}, tail={self.__tail}, length={self.__length})'
