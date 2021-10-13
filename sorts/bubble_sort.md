# 冒泡排序

![](.\img\bubble_sort.gif)

### 算法描述

1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；

2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；

3. 针对所有的元素重复以上的步骤，除了最后一个；

4. 重复步骤1~3，直到排序完成。

### 代码

```python
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
```

