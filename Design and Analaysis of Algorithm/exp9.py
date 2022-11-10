# Design and implement in Java to find a subset of a given set S = {Sl, S2, ....., Sn} of n positive integers 
# whose SUM is equal to a given positive integer d. For example, if S = {1, 2, 5, 6, 8} and d= 9, there are two 
# solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution.

def findSubset(S, d):
    n = len(S)
    collector = []
    possible = []
    for i in range(2**n):
        collector.append([])
        sum = 0
        for j in range(n):
            if (i & (1 << j)):
                collector[i].append(S[j])
                sum += S[j]
        if sum == d:
            possible.append(collector[i])
    return possible

if __name__ == "__main__":
    S = [1, 2, 5, 6, 8]
    d = 7
    ans = findSubset(S, d)
    if (len(ans) == 0):
        print("No solution")
    else:
        print("Possible Solutions are: ", end="")
        for i in ans:
            print(i, end=" ")
        