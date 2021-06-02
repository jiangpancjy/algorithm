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

    def partition(self, collection, left_index, right_index):
        pivot = collection[left_index]
        while left_index < right_index:
            while left_index < right_index and collection[right_index] >= pivot:
                right_index -= 1
            collection[left_index] = collection[right_index]

            while left_index < right_index and collection[left_index] <= pivot:
                left_index += 1
            collection[right_index] = collection[left_index]

        collection[left_index] = pivot
        return left_index

    def quick_sort1(self, collection, left_index, right_index):
        if left_index < right_index:
            index_of_pivot = self.partition(collection, left_index, right_index)
            self.quick_sort1(collection, left_index, index_of_pivot-1)
            self.quick_sort1(collection, index_of_pivot+1, right_index)
            return collection
        return collection

    def selection_sort(self, collection):
        length = len(collection)
        for i in range(length):
            index_of_min_elem = i
            for j in range(i, length - 1):
                if collection[index_of_min_elem] > collection[j + 1]:
                    index_of_min_elem = j + 1
            collection[i], collection[index_of_min_elem] = collection[index_of_min_elem], collection[i]
        return collection
