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

    def quick_sort2(self, collection, left_index, right_index):
        l, r = left_index, right_index
        if l < r:
            index_of_pivot = self.partition(collection, l, r)
            self.quick_sort2(collection, l, index_of_pivot-1)
            self.quick_sort2(collection, index_of_pivot+1, r)
            return collection
        return collection

    def selection_sort(self, collection):
        length = len(collection)
        for i in range(length):
            index_of_min_elem = i
            for j in range(i + 1, length):
                if collection[index_of_min_elem] > collection[j]:
                    index_of_min_elem = j
            collection[i], collection[index_of_min_elem] = collection[index_of_min_elem], collection[i]
        return collection

    def insert_sort(self, collection):
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
