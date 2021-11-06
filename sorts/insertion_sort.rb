def insertion_sort(array)
    # 插入算法的代码实现
    # :param array: 一个数组
    # :return: 一个升序的数组
    for i in 1...array.length
        j = i
        while j > 0 do
            if array[j] < array[j - 1]
                array[j], array[j - 1] = array[j - 1], array[j]
            else
                break
            end
            j -= 1
        end
    end
    return array
end

def insertion_sort2(array)
    # 插入排序算法的代码实现-升级版
    # :param array: 一个数组
    # :return: 一个升序数组
    for i in 0...(array.length - 1)
        temp_index = i
        insert_value = array[i + 1]
        while i >= 0 and insert_value < array[i] do
            array[i + 1] = array[i]
            i -= 1
        end
        if i != temp_index
            array[i + 1] = insert_value
        end
    end
    return array
end
