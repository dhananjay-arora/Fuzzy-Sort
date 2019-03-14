import time
def partition(array, array2, low, high):

    if low < high:
        j = quick_sort(array,array2,low,high)
        partition(array,array2,low,j-1)
        partition(array,array2,j+1,high)


def quick_sort(array, array2,low, high):
    pivot = array[low]
    i=low+1
    j=high
    
    while(i<j):
        while(array[i] <= pivot and i<=high):
            i+=1
        while(array[j] > pivot and j>=low+1):
            j-=1
        if i<j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            temp = array2[i]
            array2[i] = array2[j]
            array2[j] = temp


            
    temp = array[low]
    array[low] = array[j]
    array[j] = temp

    temp = array2[low]
    array2[low] = array2[j]
    array2[j] = temp


    return j;
    

array = [6,9,13,3,11,13,12,14,9,5,7,1,1,6]
array2 = [7,11,14,7,15,14,14,15,15,7,9,5,9,10]
start_time = time.time()
partition(array, array2, 0, len(array)-1)
end_time = time.time()

print("Time Taken by quick sort is: ",end_time-start_time)
print("Quick Sorted Output array A is as follows" , array)
print("Quick Sorted Output array B is as follows" , array2)
