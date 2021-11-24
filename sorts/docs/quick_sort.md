# 快速排序

快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

![](img/quick_sort.gif)

### 算法描述

快速排序使用分治法来把一个数组 (array) 分为两个子数组 (sub-array)。具体算法描述如下：

1. 从数列中挑出一个元素，称为 “基准” (pivot)；

2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面 (相同的数可以到任一边)。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区 (partition) 操作；

3. 递归地 (recursive) 把小于基准值元素的子数组和大于基准值元素的子数组排序。

### 代码

```python
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
```

