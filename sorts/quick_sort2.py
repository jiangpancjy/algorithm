def partition(array, left_index, right_index):
    """
    以数组第一个元素作为基准元素，将比基准小的元素放在数组左侧，
    比基准大的元素放在数组右侧，最后将基准元素放在两者之间（如
    果这个基准是数组中的最小值或最大值，则放在数组最左侧或最右侧）
    :param array: 一个数组
    :param left_index: 数组的左边界，起始通常是 0
    :param right_index: 数组的右边界，起始通常是数组长度 - 1
    :return: 返回基准元素的位置
    """
    l, r = left_index, right_index
    pivot = array[l]
    while l < r:
        while l < r and array[r] >= pivot:
            r -= 1
        array[l] = array[r]

        while l < r and array[l] <= pivot:
            l += 1
        array[r] = array[l]

    array[l] = pivot
    return l


def quick_sort2(array, left_index, right_index):
    """
    快速排序算法的代码实现
    :param array: 一个数组
    :param left_index: 数组的左边界，起始通常是 0
    :param right_index: 数组的右边界，起始通常是数组长度 - 1
    :return: 一个升序数组
    """
    l, r = left_index, right_index
    if l < r:
        index_of_pivot = partition(array, l, r)
        quick_sort2(array, l, index_of_pivot - 1)
        quick_sort2(array, index_of_pivot + 1, r)
        return array
    return array
