def insertion_sort(array):
    """
    插入排序算法的代码实现
    :param array: 一个数组
    :return: 一个升序数组
    """
    for i in range(1, len(array)):
        j = i
        while j > 0:
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
            j -= 1
    return array


def insertion_sort2(array):
    """
    插入排序算法的代码实现-升级版
    :param array: 一个数组
    :return: 一个升序数组
    """
    for insert_index, insert_value in enumerate(array[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < array[insert_index]:
            array[insert_index + 1] = array[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            array[insert_index + 1] = insert_value
    return array
