def partition(collection, left_index, right_index):
    l, r = left_index, right_index
    pivot = collection[l]
    while l < r:
        while l < r and collection[r] >= pivot:
            r -= 1
        collection[l] = collection[r]

        while l < r and collection[l] <= pivot:
            l += 1
        collection[r] = collection[l]

    collection[l] = pivot
    return l


def quick_sort2(collection, left_index, right_index):
    l, r = left_index, right_index
    if l < r:
        index_of_pivot = partition(collection, l, r)
        quick_sort2(collection, l, index_of_pivot - 1)
        quick_sort2(collection, index_of_pivot + 1, r)
        return collection
    return collection
