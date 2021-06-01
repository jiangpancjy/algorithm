class Sort:

    def bubble_sort(self, collection):
        """
        Pure implementation of bubble sort algorithm in Python
        :param collection: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        """
        length = len(collection)
        swapped = False
        for i in range(length):
            for j in range(length - 1 - i):
                if collection[j] > collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break  # Stop iteration if the collection is sorted.
        return collection

    def quick_sort(self, collection):
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
        return self.quick_sort(small_elements) + [pivot] + self.quick_sort(big_elements)
