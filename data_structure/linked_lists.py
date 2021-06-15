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
        current_pos = 0
        current_node = self.head
        while current_pos < pos:
            current_node = current_node.next
            current_pos += 1
        return current_node.value

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

    def insert_from_head(self, value):
        """
        Insert node from the head of the linked list
        :param value: The value of the node to be inserted
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_from_tail(self, value):
        """
        Insert node from the tail of the linked list
        :param value: The value of the node to be inserted
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        prev = self.head
        while prev.next is not None:
            prev = prev.next
        prev.next = node

    def insert_from_pos(self, pos, value):
        """
        Insert a node from the specified position of the linked list
        :param pos: The position of the node to be inserted
            you can input Non-negative integer(0, 1, 2, ……)
        :param value: The value of the node to be inserted
        """
        node = Node(value)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        i = 1
        current_node = self.head
        while current_node is not None:
            if i == pos:
                node.next = current_node.next
                current_node.next = node
                return
            else:
                current_node = current_node.next
                i += 1
        print("Position out of range")

    def remove_from_head(self):
        """
        Remove node from the head of the linked list
        """
        if self.head is None:
            print("Linked list has no element")
            return
        self.head = self.head.next

    def remove_from_tail(self):
        """
        Remove node from the tail of the linked list
        """
        if self.head is None:
            print("Linked list has no element")
            return
        pre = self.head
        while pre.next.next is not None:
            pre = pre.next
        pre.next = None

    def remove_from_pos(self, pos):
        """
        Delete the node of the specified sequence number from the linked list
        :param pos: The sequence number of the node to be deleted
            you can input positive integer(1, 2, 3, ……)
        """
        if self.head is None:
            print("Linked list has no element")
            return
        if pos == 0:
            print("Please input positive integer")
            return
        if pos == 1:
            self.head = self.head.next
            return
        current_node = self.head
        i = 1
        while i < pos - 1:
            if current_node.next.next is None:
                break
            current_node = current_node.next
            i += 1
        if pos - i > 1:
            print("Sequence out of range")
            return
        if current_node.next.next is None:
            current_node.next = None
        else:
            current_node.next = current_node.next.next
