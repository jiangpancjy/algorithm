"""
括号匹配
"""
from data_structure.stack.stacks import Stack


class Solution:

    def is_valid(self, strings):
        stack = Stack()
        for string in strings:
            if string == "(":
                stack.push(string)
            else:
                if stack.is_empty():
                    return False
                else:
                    stack.pop()
        else:
            if stack.is_empty():
                return True
            else:
                return False
