"""
题目描述：
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
"""


def special_sort(string):
    length = len(string)
    i = 0
    list_ = list(string)
    while i < length:
        j = 0
        while j < length - 1 - i:
            k = j + 1
            if 90 < ord(list_[j]) < 97 or ord(list_[j]) > 122 or ord(list_[j]) < 65:
                j += 1
                k += 1
            elif 90 < ord(list_[k]) < 97 or ord(list_[k]) > 122 or ord(list_[k]) < 65:
                k += 1
            if 65 <= ord(list_[j]) <= 90:
                if 65 <= ord(list_[k]) <= 90:
                    if ord(list_[j]) > ord(list_[k]):
                        list_[j], list_[k] = list_[k], list_[j]
                        j = k
                        continue
                elif 97 <= ord(list_[k]) <= 122:
                    if ord(list_[j]) + 32 > ord(list_[k]):
                        list_[j], list_[k] = list_[k], list_[j]
                        j = k
                        continue
            elif 97 <= ord(list_[j]) <= 122:
                if 97 <= ord(list_[k]) <= 122:
                    if ord(list_[j]) > ord(list_[k]):
                        list_[j], list_[k] = list_[k], list_[j]
                        j = k
                        continue
                elif 65 <= ord(list_[k]) <= 90:
                    if ord(list_[j]) - 32 > ord(list_[k]):
                        list_[j], list_[k] = list_[k], list_[j]
                        j = k
                        continue
            j = k
        i += 1
    return "".join(list_)


if __name__ == '__main__':
    print(special_sort("Bab?A"))
    print(special_sort("Ba?bA"))
    print(special_sort("ZcB.ab/A"))
