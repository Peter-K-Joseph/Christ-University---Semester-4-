def knapsack(max_weight, data):
    dataset = []
    dataset_dash = []
    print(data)

    for i in range(0, len(data)):
        for j in dataset_dash:
            if (dataset.count(j) == 0):
                dataset.append(j)
        if (i == 0):
            dataset.append([0, 0])
        else:
            for j in dataset_dash:
                if (dataset.count(j) == 0):
                    dataset.append([data[i-1][0], data[i-1][1]])
        # if (i != 0 or dataset_dash[i-1][1] > dataset[i][1]):
        #     dataset.pop()
        dataset_dash.append([dataset[i][0] + data[i][0], dataset[i][1] + data[i][1]])
        

def numcheck(num):
    if (str(num).isdigit() and num != ''):
        return True
    else:
        return False


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
        dataset.append(([int(profit), int(weight)]))
        count += 1
    proceed = input("Do you want to enter another item? (y/n): ")
knapsack(int(capacity), dataset)
