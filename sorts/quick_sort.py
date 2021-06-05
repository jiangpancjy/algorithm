def quick_sort(collection):
    """
    Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    if len(collection) < 2:
        return collection
    pivot = collection.pop()
    big_elements = list()
    small_elements = list()
    for element in collection:
        if element > pivot:
            big_elements.append(element)
        else:
            small_elements.append(element)
    return quick_sort(small_elements) + [pivot] + quick_sort(big_elements)
