#importing all the sorting python files
import time
import mergesort
import heapsort
import quicksort
import insertionsort
import bubble
import selectionsort
import numpy as np
import matplotlib.pyplot as plt

def main():
    #getting the input from the user
    arr = []
    i = 0
    size = int (input ("Enter the array size : "))

    for i in range (size):
        value = int (input ("Enter the  Element %d of List : " % i))
        arr.append (value)
    # creating copies to call different classes
    array1 = arr.copy ()
    array2 = arr.copy ()
    array3 = arr.copy ()
    array4 = arr.copy ()
    array5 = arr.copy()
    array6 = arr.copy()
    array7 = arr.copy()

    # calling and calculating the time for insertion sort
    I = insertionsort.insertion ()
    istart_time = time.perf_counter ()
    r = I.insertionsort (array5,size)
    Insertion_time = time.perf_counter () - istart_time
    print ("Insertion sort results:", r)
    print ("Insertion sort Runtime=", Insertion_time)

    # calling and calculating the time for bubble sort
    B = bubble.Bubble ()
    bstart_time = time.perf_counter ()
    r = B.bubbleSort (array6, size)
    bubble_time = time.perf_counter () - bstart_time
    print ("Bubble sort results:", r)
    print ("Bubble sort Runtime=", bubble_time)

    # calling and calculating the time for selection sort
    S = selectionsort.selection ()
    sstart_time = time.perf_counter ()
    r = S.selectionSort (array7, size)
    selection_time = time.perf_counter () - sstart_time
    print ("Selection sort results:", r)
    print ("Selection sort Runtime=", selection_time)

    # calling and calculating the time for merge sort
    M=mergesort.merge()
    mstart_time = time.perf_counter ()
    r=M.mergesort(array1)
    merge_time = time.perf_counter() - mstart_time
    print("Merge sort results:",r)
    print ("Merge sort Runtime=", merge_time)

    # calling and calculating the time for heap sort
    H = heapsort.heap ()
    hstart_time = time.perf_counter ()
    r = H.heapSort (array2)
    heap_time = time.perf_counter () - hstart_time
    print ("Heap Sort results:", r)
    print ("Heap sort Runtime=", heap_time)


    # calling and calculating the time for quicksort
    Q = quicksort.quick ()
    qstart_time = time.perf_counter ()
    r = Q.quickSort (array3,size-1,0)
    quick_time = time.perf_counter () - qstart_time
    print ("Quick Sort results:", r)
    print ("Quick sort Runtime=", quick_time)

    # calling and calculating the time for quicksort using 3 median sort
    Q = quicksort.quick ()
    qmstart_time = time.perf_counter ()
    r = Q.quickSort_median_of_three (array4, 0,size)
    quickm_time = time.perf_counter () - qmstart_time
    print ("Quick Sort Median of three results:", r)
    print ("Quick sort  Median of three Runtime=", quickm_time)

#create an array to store the calculated time
    x = []
    x.append (bubble_time)
    x.append (Insertion_time)
    x.append (selection_time)
    x.append (heap_time)
    x.append (merge_time)
    x.append (quick_time)
    x.append (quickm_time)

#plot all the values for comparison using matplotlib
    plt.xticks (np.arange (7), ('bubblesort', 'insertionsort','selectionsort', 'heapsort', 'mergesort', 'quicksort','quicksort using median'))
    plt.plot (x, 'bo', x, 'r')
    plt.show()
main()