def bubble_sort(array)
    # 冒泡排序算法的代码实现
    # :param array: 一个数组
    # :return: 一个升序数组
    length = array.length
    for i in 0...(length - 1)
        is_swapped = false
        for j in 0...(length - 1 - i)
            if array[j] > array[j + 1]
                is_swapped = true
                array[j], array[j + 1] = array[j + 1], array[j]
            end
        end
        if not is_swapped
            break
        end
    end
    return array
end
