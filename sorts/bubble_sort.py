def bubble_sort(array):
    """
    冒泡排序算法的代码实现
    :param array: 一个数组
    :return: 一个升序数组
    """
    length = len(array)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break  # 如果数组已经是升序，则停止迭代
    return array
