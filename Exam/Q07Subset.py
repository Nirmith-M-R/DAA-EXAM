#7 Dynamic Programming O(n*W+1)
def subset(weights, W):
    n = len(weights)
    M = [[0]*(W+1) for i in range(n+1)]

    for i in range(1,n+1):
        for w in range(W+1):
            if weights[i-1]>w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], M[i-1][w - weights[i-1]]+weights[i-1])
    
    maxweight = M[n][W]
    selected = []
    w = W
    for i in range(n,0,-1):
        if M[i][w] != M[i-1][w]:
            selected.append(i)
            w-=weights[i-1]
    return maxweight, selected

n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i+1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

maxWeight, selected = subset(weights, W)
print("Maximum weight: ",maxWeight)
print("Items selected are: ",selected)