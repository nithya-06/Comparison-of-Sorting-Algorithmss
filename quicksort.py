class quick:
    #function for quick sort
    def partition(object,array, lowelement, highelement):
        counter = (lowelement - 1)
        # choose the highest element as pivot element
        pivot = array[highelement]

        for j in range (lowelement, highelement):

            # if the pivot is greater than or equal to current element
            if array[j] <= pivot:
                # increment counter
                counter = counter + 1
                #call swap function using object
                object.swap (array, counter, j)

        object.swap (array, counter + 1, highelement)
        return (counter + 1)
#function for swapping
    def swap(object,arra, i, j):
        arra[i], arra[j] = arra[j], arra[i]
#function for  partitioning the values for quick sort using median of 3 approach
    def partition_median_of_three(object,a, first, end):
        med = int (end - 1 - first) // 2
        med = med + first
        l = first + 1
        if (a[med] - a[end - 1]) * (a[first] - a[med - 1]) >= 0:
            object.swap (a, first, med)
        elif (a[end - 1] - a[med]) * (a[first] - a[end - 1]) >= 0:
            object.swap (a, first, end)
        pivot = a[first]#here pivot is the first element
        for r in range (first, end):
            if pivot > a[r]:
                object.swap (a, l, r)
                l = l + 1
        object.swap (a, first, l - 1)
        return l - 1
#function for quicksort using median of 3 approach
    def quickSort_median_of_three(object, a, first, end):
        if first < end:
            splitPoint = object.partition_median_of_three (a, first, end)
            object.quickSort_median_of_three ( a, first, splitPoint)
            object.quickSort_median_of_three ( a, splitPoint + 1, end)
        return a

    # Function to do Quick sort
    def quickSort(object, array, last, first):
        if first < last:
            pivot = object.partition (array, first, last)

            # Separately sort elements before and after the pivot
            object.quickSort ( array, pivot - 1, first)
            object.quickSort ( array, last, pivot + 1)
        return array




