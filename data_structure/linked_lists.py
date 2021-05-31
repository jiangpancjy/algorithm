class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "head->None"
        str_ = "head->"
        curr = self.head
        while curr.next is not None:
            str_ += "{}->".format(curr.val)
            curr = curr.next
        return str_ + str(curr.val)

    def insert_from_head(self, val):
        """
        Insert node from the head of the linked list
        :param val: The value of the node to be inserted
        """
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_from_tail(self, val):
        """
        Insert node from the tail of the linked list
        :param val: The value of the node to be inserted
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            return

        prev = self.head
        while prev.next is not None:
            prev = prev.next
        prev.next = node

    def insert_from_pos(self, pos, val):
        """
        Insert a node from the specified position of the linked list
        :param pos: The position of the node to be inserted
            you can input Non-negative integer(0, 1, 2, ……)
        :param val: The value of the node to be inserted
        """
        node = Node(val)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        i = 1
        curr = self.head
        while curr is not None:
            if i == pos:
                node.next = curr.next
                curr.next = node
                return
            else:
                curr = curr.next
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

    def remove_from_seq(self, seq):
        """
        Delete the node of the specified sequence number from the linked list
        :param seq: The sequence number of the node to be deleted
            you can input positive integer(1, 2, 3, ……)
        """
        if self.head is None:
            print("Linked list has no element")
            return
        if seq == 0:
            print("Please input positive integer")
            return
        if seq == 1:
            self.head = self.head.next
            return
        curr = self.head
        i = 1
        while i < seq - 1:
            if curr.next.next is None:
                break
            curr = curr.next
            i += 1
        if seq - i > 1:
            print("Sequence out of range")
            return
        if curr.next.next is None:
            curr.next = None
        else:
            curr.next = curr.next.next

    def list_2_linked_list(self, item):
        if not isinstance(item, list):
            print("Please input a list")
            return
        self.head = curr = Node(item[0])
        for i in range(1, len(item)):
            curr.next = Node(item[i])
            curr = curr.next
