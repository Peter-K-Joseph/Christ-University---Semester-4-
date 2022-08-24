import numpy as np
# Dynamic using box approach

def numcheck(num):
    if (str(num).isdigit() and num != ''):
        return True
    else:
        return False
  
def getMax(dataset, profit, weights, i , j):
    value_1 = dataset[i-1][j]
    value_2 = dataset[i-1][j-weights[i]] + int(profit[i])
    print("value_1: {} value_2: {}".format(value_1, value_2))
    if (j-weights[i] < 0):
        return value_1
    elif (value_1 > value_2):
        return value_1
    else:
        return value_2

def knapsack(max_weight, weights, profit, length):
    dataset = []
    for i in range(0, length+1):
        dataset.append([])
        for j in range(0, max_weight+1):
            dataset[i].append(0)     
    
    for i in range(0, length):
        for j in range(0, max_weight+1):
            dataset[i][j] = getMax(dataset, profit, weights, i, j)
            
    print("          ", end="")
    for i in range(0, max_weight+1):
        print("W{}".format(i), end="\t")
    print("")
    
    for i in range(0, len(dataset)-1):
        initrun = True
        for j in dataset[i]:
            if (initrun == True):
                print("Pi{} Wi{}    ".format(profit[i], weights[i]), end="")
                initrun = False        
            print(j, end="\t")
        print("")
    
    
capacity = input("Enter maximum number of weight: ")
dataset = []
proceed = 'y'
count = 0
while (proceed == 'y' or proceed == 'Y'):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))
    if (numcheck(weight) == False and numcheck(profit) == False):
        print("Invalid input. Please enter again.")
        continue
    else:
        dataset.append(([count+1, int(weight), int(profit)]))
        count += 1
    proceed = input("Do you want to enter another item? (y/n): ")
numpy_array = np.array(dataset)
knapsack(int(capacity), numpy_array[:,1], numpy_array[:,2], len(numpy_array))