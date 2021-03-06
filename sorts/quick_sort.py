def quick_sort(array):
    """
    快速排序算法的代码实现
    :param array: 一个数组
    :return: 一个升序数组
    """
    if len(array) < 2:
        return array
    pivot = array.pop()
    big_elements = list()
    small_elements = list()
    for element in array:
        (big_elements if element > pivot else small_elements).append(element)
    return quick_sort(small_elements) + [pivot] + quick_sort(big_elements)


def partition(array, left_index, right_index):
    """
    分区函数
    :param array: 一个数组
    :param left_index: 数组的左边界，起始通常是 0
    :param right_index: 数组的右边界，起始通常是数组长度 - 1
    :return: 返回基准元素的位置
    """
    pivot = array[left_index]
    while left_index < right_index:
        while left_index < right_index and pivot <= array[right_index]:
            right_index -= 1
        if left_index < right_index:
            array[left_index] = array[right_index]
            left_index += 1
        while left_index < right_index and pivot >= array[left_index]:
            left_index += 1
        if left_index < right_index:
            array[right_index] = array[left_index]
            right_index -= 1
    array[left_index] = pivot
    return left_index


def quick_sort2(array, left_index, right_index):
    """
    快速排序算法的代码实现2
    :param array: 一个数组
    :param left_index: 数组的左边界，起始通常是 0
    :param right_index: 数组的右边界，起始通常是数组长度 - 1
    :return: 一个升序数组
    """
    if left_index < right_index:
        pivot_index = partition(array, left_index, right_index)
        quick_sort2(array, left_index, pivot_index - 1)
        quick_sort2(array, pivot_index + 1, right_index)
        return array
    return array
