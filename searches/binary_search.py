from typing import List


def binary_search(array: List[int], num: int) -> int:
    """
    二分查找算法的代码实现
    :param array: 一个升序数组
    :param num: 一个数
    :return: 如果在数组中找到值对应的元素，则返回其位置；否则返回 -1
    """
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1
