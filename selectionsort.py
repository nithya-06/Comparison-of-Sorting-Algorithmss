class selection:
    #function for selection sort
    def selectionSort(object, array, size):
        for i in range (size):
            mini = i
            for j in range (i + 1, size):
                if array[mini] > array[j]:
                    mini = j

            array[i], array[mini] = array[mini], array[i]
        return array

#return the sorted array
        return array


