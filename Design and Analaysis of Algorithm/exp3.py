# Knapsack Problem By Greedy Approach

def numcheck(num):
    if (num.isdigit() and num != ''):
        return True
    else:
        return False

max = input("Enter maximum number of weight: ")
dataset = []
proceed = 'y'
count = 0
while (proceed == 'y' or proceed == 'Y'):
    weight = input("Enter weight: ")
    profit = input("Enter profit: ")
    if (numcheck(weight) == False and numcheck(profit) == False):
        print("Invalid input. Please enter again.")
        continue
    else:
        dataset.append(([count+1, int(weight), int(profit), int(profit)/int(weight)]))
        count += 1
    proceed = input("Do you want to enter another item? (y/n): ")
dataset.sort(key=lambda x: x[2]/x[1], reverse=True)
profit = {
    "max_profit": 0,
    "left": int(max),
    "selected": []
}
for arrays in dataset:
    temp = profit["left"]
    temp = temp - arrays[1]
    if (temp < 0):
        if (profit["left"] <= 0):
            continue
        greedy_weight = profit["left"]/arrays[1]
        greedy_profit = greedy_weight * arrays[2]
        profit["max_profit"] += greedy_profit
    else:
        profit["max_profit"] += arrays[2]
    profit["left"] = temp
    profit["selected"].append(arrays[0])
print("Maximum profit: ", profit["max_profit"])
print("Items selected: ", profit["selected"])