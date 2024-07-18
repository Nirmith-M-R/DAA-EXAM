#6 Dynamic Programming 
def weighted(x):
    if x == 0:
        return 0
    elif M[x-1]:
        return M[x-1]
    else:
        M[x-1] = max(weighted(x-1), weighted(p[x-1])+interval[x-1][2])
        return M[x-1]
    
def selection(k):
    if k<1:
        return
    i = k
    while i>1 and M[i-1]==M[i-2]:
        i-=1
    selected.append(interval[i-1])
    selection(p[i-1])

n = int(input("Enter number of intervals: "))
interval = []
for i in range(n):
    interval.append(list(map(int, input("start, end, val: ").split())))

interval.sort(key = lambda item:item[1])
p = [0]*n
for i in range(n-1,0,-1):
    for j in range(i-1,-1,-1):
        if interval[i][0] >= interval[j][1]:
            p[i] = j+1
            break

M = [0]*n
selected = []
print("MaxProfit: ", weighted(n))
selection(n)
print("Selected: ",selected)