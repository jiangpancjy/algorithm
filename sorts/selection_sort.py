def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        index_of_min_elem = i
        for j in range(i + 1, length):
            if collection[index_of_min_elem] > collection[j]:
                index_of_min_elem = j
        collection[i], collection[index_of_min_elem] = collection[index_of_min_elem], collection[i]
    return collection
