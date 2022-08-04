import random
import timeit
import csv

def quicksort(start, end):
    global array
    if (start < end):
        p = partition(start, end)
        quicksort(start, p-1)
        quicksort(p+1, end)

def partition(start, end):
    global array
    pivot = array[end]
    i = start-1
    for j in range(start, end):
        if (array[j] < pivot):
            i = i+1
            swap(i, j)
    swap(i+1, end)
    return i+1

def swap(i, j):
    global array
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sort():
    start = timeit.default_timer()
    for i in range(0, limiter):
        array.append(random.randint(1, 50000))
    quicksort(0, len(array)-1)
    stop = timeit.default_timer()
    return [stop - start, len(array)]

writer = csv.writer(open("file.csv", "a"), lineterminator='\n')
time = []
limiter = 5000
for i in range(0, 100):
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