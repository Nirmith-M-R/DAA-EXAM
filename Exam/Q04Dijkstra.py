#4 Greedy O((v+e)logv)
def min_distance(dist, sptset):
    minindex = -1
    minval= float('Inf')
    for i in range(len(sptset)):
        if not sptset[i] and dist[i]<minval:
            minval = dist[i]
            minindex = i
    return minindex

def dijkstra(graph,src):
    dist = [float("Inf")]*len(graph)
    dist[src]=0
    sptset = [False]*len(graph)

    for i in range(len(graph)):
        u = min_distance(dist,sptset)
        sptset[u]=True

        for j in range(len(graph)):
            if graph[i][j]>0 and dist[j]>dist[u]+graph[u][j] and not sptset[j]:
                dist[j] = dist[u]+graph[u][j]
    
    print("Vertex | Distance")
    for i in range(len(dist)):
        print("  ",i, "\t",dist[i])

graph = [
    [0,  10,  0,  0, 100],
    [10,  0, 50,  0,  10],
    [0,  50,  0, 20,   0],
    [0,   0, 20,  0,  60],
    [100, 10, 0,  60,  0]
]

dijkstra(graph, 0)