from typing import List


def binary_search(array: List[int], num: int) -> int:
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
