"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
"""
from data_structure.stack.stacks import Stack


class Solution:

    def is_valid(self, strings):
        stack = Stack()
        for string in strings:
            if string in "([{":
                stack.push(string)
            else:
                if stack.is_empty():
                    return False
                elif self._match(stack.peek(), string):
                    stack.pop()
                else:
                    return False
        else:
            if stack.is_empty():
                return True
            else:
                return False

    def _match(self, left_bracket, right_bracket):
        if "([{".index(left_bracket) == ")]}".index(right_bracket):
            return True
        return False
