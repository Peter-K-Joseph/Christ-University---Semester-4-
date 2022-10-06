import random
import timeit
import csv

def mergeSort(arr):
    if (len(arr) == 1):
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
def sort():
    start = timeit.default_timer()
    array.append(random.randint(1, 50000, limiter))
    mergeSort(array)
    stop = timeit.default_timer()
    return [stop - start, len(array)]
        
if __name__ == '__main__':
    writer = csv.writer(open("file.csv", "a"), lineterminator='\n')
    time = []
    limiter = 5000
    for i in range(0, 1):
        average_time = []
        size = 0
        for j in range(0, 7):
            array = []
            data = sort()
            size = data[1]
            print("Ran {0} times of 10 for position {1}.".format(j, str(size)))
            average_time.append(data[0])
        print("[!] At Position {0}. Runtime {1}. Left {2}".format(str(size), str(sum(average_time)/len(average_time)), 100-i))
        time.append([str(size), str(sum(average_time)/len(average_time))])
        limiter=limiter+20000
    writer.writerows(time)