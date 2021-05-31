import time
class insertion:
#function for insertion sort
    def insertionsort(object, a, size):

        for i in a:
            j = a.index (i)

            while j > 0:

                if a[j - 1] > a[j]:
                    # swap using temp varaible
                    temp = a[j - 1]
                    a[j - 1] = a[j]
                    a[j] = temp
                else:

                    break
                j = j - 1

    #return the sorted array
        return a

#arr = []
#i = 0
#size = int (input ("Enter the array size : "))

#for i in range (size):
#    value = int (input ("Enter the  Element %d of List : " % i))
#    arr.append (value)
#istart_time = time.perf_counter ()
#r=insertion.insertionsort(object,arr,size)
#Insertion_time = time.perf_counter () - istart_time
#print ("Insertion sort results:", r)
#print ("Insertion sort Runtime=", Insertion_time)