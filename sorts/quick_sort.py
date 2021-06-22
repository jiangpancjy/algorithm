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
        if element > pivot:
            big_elements.append(element)
        else:
            small_elements.append(element)
    return quick_sort(small_elements) + [pivot] + quick_sort(big_elements)
