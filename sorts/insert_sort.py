def insert_sort(array):
    """
    插入排序算法的代码实现
    :param array: 一个数组
    :return: 一个升序数组
    """
    i = 1
    while i < len(array):
        j = i - 1
        k = i
        while j >= 0:
            if array[k] < array[j]:
                array[k], array[j] = array[j], array[k]
                j -= 1
                k -= 1
            else:
                break
        i += 1
    return array
