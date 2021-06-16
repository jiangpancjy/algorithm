class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, seq=None):
        if seq is None:
            self._length = 0
            self.head = None
        else:
            seq_length = len(seq)
            self._length = seq_length
            self.head = current_node = Node(seq[0])
            for i in range(1, seq_length):
                current_node.next = Node(seq[i])
                current_node = current_node.next

    def __getitem__(self, pos):
        self._check_index(pos)
        i = 0
        current_node = self.head
        while i < pos:
            current_node = current_node.next
            i += 1
        return current_node.value

    def __setitem__(self, pos, value):
        self._check_index(pos)
        i = 0
        current_node = self.head
        while i < pos:
            current_node = current_node.next
            i += 1
        current_node.value = value

    def __len__(self):
        return self._length

    def __str__(self):
        if self.head is None:
            return "head->None"
        string = "head->"
        current_node = self.head
        while current_node.next is not None:
            string += f"{current_node.value}->"
            current_node = current_node.next
        return string + str(current_node.value)

    def _check_index(self, pos):
        if not isinstance(pos, int):
            raise TypeError('Index must be an integer')
        if pos >= self._length:
            raise IndexError('Index out of range')
        if pos < 0:
            raise IndexError('Index must be positive')

    def append(self, value):
        """
        Insert node from the tail of the linked list
        :param value: The value of the node to be inserted
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self._length = 1
            return

        prev = self.head
        while prev.next is not None:
            prev = prev.next
        prev.next = node
        self._length += 1

    def insert(self, pos, value):
        """
        Insert a node from the specified position of the linked list
        :param pos: The position of the node to be inserted
            you can input Non-negative integer(0, 1, 2, ……)
        :param value: The value of the node to be inserted
        """
        self._check_index(pos)
        node = Node(value)
        if pos == 0:
            node.next = self.head
            self.head = node
            self._length += 1
            return
        
        i = 1
        current_node = self.head
        while i < pos:
            current_node = current_node.next
            i += 1
        node.next = current_node.next
        current_node.next = node
        self._length += 1
        return
