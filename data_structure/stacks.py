class Stack:

    def __init__(self):
        """使用列表来实现栈"""
        self._values = []

    def __len__(self):
        """返回栈的长度"""
        return len(self._values)

    def push(self, v):
        """压栈"""
        self._values.append(v)

    def pop(self):
        """出栈"""
        self._values.pop()

    def peek(self):
        """检视栈顶元素"""
        if not self._values:
            return None
        return self._values[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return self._values == []
