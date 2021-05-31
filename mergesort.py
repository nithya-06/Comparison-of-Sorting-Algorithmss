import time

class merge:
    #function for mergesort
    def mergesort(object, a):
#finding the length of array
        lengthofarr = len (a)
        if lengthofarr > 1:
            midelement = lengthofarr // 2
            l = a[:midelement]
            r = a[midelement:]
            lengthofl = len (l)
            lengthofr = len (r)
            #call the mergesort recursively for the left and right arrays
            merge.mergesort (object, l)
            merge.mergesort (object, r)
            i = 0
            j = 0
            k = 0
            while i < lengthofl and j < lengthofr:
                if l[i] < r[j]:
                    a[k] = l[i]
                    i += 1
                else:
                    a[k] = r[j]
                    j += 1
                k += 1

            while j < lengthofr:
                a[k] = r[j]
                j += 1
                k += 1

            while i < lengthofl:
                a[k] = l[i]
                i += 1
                k += 1
#return the sorted array
        return a


arr = []
i = 0
size = int (input ("Enter the array size : "))

for i in range (size):
    value = int (input ("Enter the  Element %d of List : " % i))
    arr.append (value)
mstart_time = time.perf_counter ()
r=merge.mergesort(object,arr)
merge_time = time.perf_counter() - mstart_time
print("Merge sort results:",r)
print ("Merge sort Runtime=", merge_time)



