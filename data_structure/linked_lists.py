from utils.constants import MethodType


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prev = None


class LinkedList:

    def __init__(self, seq=None):
        self.head = Node(value=None)
        if seq is None:
            self._length = 0
        else:
            seq_length = len(seq)
            self._length = seq_length
            self.head.next = current_node = Node(value=seq[0])
            for i in range(1, seq_length):
                current_node.next = Node(value=seq[i])
                current_node = current_node.next

    def __getitem__(self, pos):
        self._check_pos(pos)
        return self._traverse(pos).next.value

    def __setitem__(self, pos, value):
        self._check_pos(pos)
        self._traverse(pos).next.value = value

    def __len__(self):
        return self._length

    def __str__(self):
        current_node = self.head
        string = "【head】"
        while current_node.next is not None:
            current_node = current_node.next
            string += f"->【{current_node.value}】"
        return string

    def __iter__(self):
        i = 0
        current_node = self.head
        while i < self._length:
            current_node = current_node.next
            i += 1
            yield current_node

    def _check_pos(self, pos, method_type=MethodType.INDEX):
        if not isinstance(pos, int):
            raise TypeError('linked list index must be an integer')
        if method_type == MethodType.INDEX:
            if pos >= self._length or abs(pos) > self._length:
                raise IndexError('linked list index out of range')
        if method_type == MethodType.INSERT:
            if pos > self._length or abs(pos) > self._length + 1:
                raise IndexError('linked list index out of range')

    def _traverse(self, pos):
        """
        遍历链表至位置 pos 处的节点的前一个节点并返回
        :param pos: 链表中节点的位置
        :return: 位置 pos 处的节点的前一个节点
        """
        pos = self._convert_negative_2_positive(pos)
        i = 0
        previous_node = self.head
        while i < pos:
            previous_node = previous_node.next
            i += 1
        return previous_node

    def _convert_negative_2_positive(self, pos):
        """
        若位置 pos 为负数，将链表的负索引转换为正索引
        :param pos: 链表中节点的位置
        :return: 转换后的位置的 pos
        """
        if pos < 0:
            pos = self._length + pos
        return pos

    def append(self, value):
        """
        在链表尾部插入一个节点
        :param value: 要插入节点的值
        """
        self._traverse(self._length - 1).next.next = Node(value=value)
        self._length += 1

    def insert(self, pos, value):
        """
        在链表指定位置 pos 处的节点前插入一个节点
        :param pos: 链表中节点的位置
        :param value: 要插入节点的值
        """
        self._check_pos(pos, method_type=MethodType.INSERT)
        node = Node(value=value)
        previous_node = self._traverse(pos)
        node.next = previous_node.next
        previous_node.next = node
        self._length += 1

    def remove(self, value):
        """
        移除与值 value 匹配的第一个节点
        :param value: 要移除节点的值
        """
        previous_node = self.head
        for node in self:
            if node.value == value:
                previous_node.next = node.next
                node.next = None
                self._length -= 1
                return
            previous_node = node
        raise ValueError('LinkedList.remove(x): x not in LinkedList')

    def pop(self, pos=-1):
        """
        移除指定位置的节点并返回，默认移除最后一个节点
        :param pos: 链表中节点的位置
        :return: 移除的节点
        """
        self._check_pos(pos)
        previous_node = self._traverse(pos)
        current_node = previous_node.next
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node


class DoubleLinkedList(LinkedList):

    def __init__(self, seq=None, **kwargs):
        super().__init__(**kwargs)
        self.head = DoubleNode(value=None)
        self.tail = DoubleNode(value=None)
        if seq is None:
            self._length = 0
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            seq_length = len(seq)
            self._length = seq_length
            self.head.next = current_node = DoubleNode(value=seq[0])
            previous_node = self.head
            for i in range(1, seq_length):
                current_node.next = DoubleNode(value=seq[i])
                current_node.prev = previous_node
                previous_node = current_node
                current_node = current_node.next
            current_node.next = self.tail
            self.tail.prev = current_node

    def __str__(self):
        current_node = self.head
        string = "【head】"
        while current_node.next.next is not None:
            current_node = current_node.next
            string += f"<=>【{current_node.value}】"
        return string + "<=>【tail】"

    def append(self, value):
        """
        在链表尾部插入一个节点
        :param value: 要插入节点的值
        """
        current_node = DoubleNode(value=value)
        self.tail.prev.next = current_node
        current_node.prev = self.tail.prev
        self.tail.prev = current_node
        current_node.next = self.tail
        self._length += 1

    def insert(self, pos, value):
        """
        在链表指定位置 pos 处的节点前插入一个节点
        :param pos: 链表中节点的位置
        :param value: 要插入节点的值
        """
        self._check_pos(pos, method_type=MethodType.INSERT)
        node = DoubleNode(value=value)
        previous_node = self._traverse(pos)
        previous_node.next.prev = node
        node.prev = previous_node
        node.next = previous_node.next
        previous_node.next = node
        self._length += 1

    def remove(self, value):
        """
        移除与值 value 匹配的第一个节点
        :param value: 要移除节点的值
        """
        previous_node = self.head
        for node in self:
            if node.value == value:
                node.next.prev = previous_node
                node.prev = None
                previous_node.next = node.next
                node.next = None
                self._length -= 1
                return
            previous_node = node
        raise ValueError('LinkedList.remove(x): x not in LinkedList')

    def pop(self, pos=-1):
        """
        移除指定位置的节点并返回，默认移除最后一个节点
        :param pos: 链表中节点的位置
        :return: 移除的节点
        """
        self._check_pos(pos)
        previous_node = self._traverse(pos)
        current_node = previous_node.next
        current_node.next.prev = previous_node
        current_node.prev = None
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node
