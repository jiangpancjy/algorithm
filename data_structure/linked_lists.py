from utils.decorators import check_pos
from utils.constants import MethodType


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


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
            previous_node = self.head
            for i in range(1, seq_length):
                current_node.next = Node(seq[i])
                current_node.pre = previous_node
                previous_node = current_node
                current_node = current_node.next
            self.tail = current_node

    @check_pos(method_type=MethodType.INDEX)
    def __getitem__(self, pos):
        return self._traver(pos).next.value

    @check_pos(method_type=MethodType.INDEX)
    def __setitem__(self, pos, value):
        self._traver(pos).next.value = value

    def __len__(self):
        return self._length

    def __str__(self):
        current_node = self.head
        string = "head"
        while current_node.next is not None:
            current_node = current_node.next
            string += f"->({current_node.value})"
        return string + "->None"

    def _traver(self, pos):
        # TODO 写文档注释和画位置与链表的图
        if pos < 0:
            pos = self._length + pos
        i = 0
        current_node = self.head
        while i < pos:
            current_node = current_node.next
            i += 1
        return current_node

    def append(self, value):
        """
        在链表尾部插入一个节点
        :param value: 要插入节点的值
        """
        # TODO 添加前缀节点关系
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self._length += 1

    @check_pos(method_type=MethodType.INSERT)
    def insert(self, pos, value):
        """
        在链表指定位置插入一个节点
        :param pos: 节点在链表中插入的位置，类型为非负整数
        :param value: 要插入节点的值
        """
        # TODO 添加前缀节点关系
        node = Node(value)
        current_node = self._traver(pos)
        node.next = current_node.next
        current_node.next = node
        self._length += 1
