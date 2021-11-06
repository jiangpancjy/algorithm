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
