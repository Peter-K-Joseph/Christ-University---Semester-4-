# Solve the 1/0 Knapsack problem using dynamic programming.

def knapsack(capacity, weights, values):
    n = len(weights)
    memo = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                memo[i][j] = memo[i - 1][j]
    printSolution(memo, weights, values, capacity)
    return memo[n][capacity]

def printSolution(memo, weights, values, capacity):
    print("The maximum value is: ", memo[len(weights)][capacity])
    print("The items to include are: ")
    i = len(weights)
    j = capacity
    for i in range(0, len(memo)):
        for j in range(0, len(memo[i])):
            print(memo[i][j], end="\t")
        print("")
    print("\n\n\n\n")
    
    # for i in range(0, len(memo[i]) + 2):
    #     if (i == 0):
    #         print("Profit", end="\t")
    #     elif (i == 1):
    #         print("Weight", end="\t")
    #     else:
    #         print(i-2, end="\t")
    # print("")
    
    # for i in range(0, len(memo)):
    #     for j in range(0, len(memo[i]) + 2):
    #         if ((j == 0 or j == 1) and i == 0):
    #             print("0", end="\t")
    #         elif (j == 0):
    #             print(values[i - 1], end="\t")
    #         elif (j == 1):
    #             print(weights[i - 1], end="\t")
    #         else:
    #             if (memo[i][j - 2] > 0):
    #                 print("1", end="\t")
    #             else:
    #                 print("0", end="\t")
    #             # print(memo[i][j - 2], end="\t")
    #     print("")
    # print("")
    
    while i > 0 and j > 0:
        if memo[i][j] != memo[i - 1][j]:
            print("Item ", i, " with weight ", weights[i - 1], " and value ", values[i - 1])
            j = j - weights[i - 1]
        i = i - 1
        
if __name__ == "__main__":
    capacity = 8
    weights = [3,4,5,6]
    values = [2,3,4,1]
    print("The maximum value is: ", knapsack(capacity, weights, values))