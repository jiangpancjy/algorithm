def selection_sort(array):
    """
    选择排序算法的代码实现
    :param array: 一个数组
    :return: 一个升序数组
    """
    length = len(array)
    for i in range(length):
        index_of_min_elem = i
        for j in range(i + 1, length):
            if array[index_of_min_elem] > array[j]:
                index_of_min_elem = j
        array[i], array[index_of_min_elem] = array[index_of_min_elem], array[i]
    return array
