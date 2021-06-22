from utils.decorators import check_pos
from utils.constants import MethodType


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, seq=None):
        self.head = Node(None)
        if seq is None:
            self._length = 0
            self.tail = self.head
        else:
            seq_length = len(seq)
            self._length = seq_length
            self.head.next = current_node = Node(seq[0])
            for i in range(1, seq_length):
                current_node.next = Node(seq[i])
                current_node = current_node.next
            self.tail = current_node

    @check_pos(method_type=MethodType.INDEX)
    def __getitem__(self, pos):
        i = 0
        current_node = self.head.next
        while i < pos:
            current_node = current_node.next
            i += 1
        return current_node.value

    @check_pos(method_type=MethodType.INDEX)
    def __setitem__(self, pos, value):
        i = 0
        current_node = self.head.next
        while i < pos:
            current_node = current_node.next
            i += 1
        current_node.value = value

    def __len__(self):
        return self._length

    def __str__(self):
        current_node = self.head
        string = "head"
        while current_node.next is not None:
            current_node = current_node.next
            string += f"->({current_node.value})"
        return string + "->None"

    def append(self, value):
        """
        Insert node from the tail of the linked list
        :param value: The value of the node to be inserted
        """
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self._length += 1

    @check_pos(method_type=MethodType.INSERT)
    def insert(self, pos, value):
        """
        Insert a node from the specified position of the linked list
        :param pos: The position of the node to be inserted
            you can input Non-negative integer(0, 1, 2, ……)
        :param value: The value of the node to be inserted
        """
        node = Node(value)
        i = 0
        current_node = self.head
        while i < pos:
            current_node = current_node.next
            i += 1
        node.next = current_node.next
        current_node.next = node
        self._length += 1
        return
