#8 Dynamic Programming O(V*maxweight+1)
def knapsack(items, W):
    n = len(items)
    dp = [[0]*(1+W) for i in range(len(items)+1)]
    for i in range(1,len(items)+1):
        for w in range(W+1):
            if items[i-1][1]>w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]]+items[i-1][2])
    maxVal = dp[n][W]
    w = W
    selected = []
    for i in range(n,1,-1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(items[i-1])
            w-=items[i-1][1]
    return maxVal, selected

items = [(1, 5, 100),(2, 7, 300),(3, 8, 200),(4, 10, 100),(5, 5, 200),(6, 2, 100)]
maxWeight = 20
maxValue, selected = knapsack(items, maxWeight)
print("Maximum Value:", maxValue)
print("Selected Items:", selected)