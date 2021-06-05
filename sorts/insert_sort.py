def insert_sort(collection):
    i = 1
    while i < len(collection):
        j = i - 1
        k = i
        while j >= 0:
            if collection[k] < collection[j]:
                collection[k], collection[j] = collection[j], collection[k]
                j -= 1
                k -= 1
            else:
                break
        i += 1
    return collection
