#9 Dynamic Programming O(n^2)
def bellman(graph,src, V):
    n = len(graph)
    dist = [float("Inf")]*(n)
    dist[src]=0

    for i in range(V-1):
        for edge in graph:
            if dist[edge[1]]>dist[edge[0]]+edge[2]:
                dist[edge[1]]=dist[edge[0]]+edge[2]

    for e in edge:
        if dist[edge[1]]>dist[edge[0]]+edge[2]:
            print("Graph has negative edge.")
            return
        
    print("Vertex | Distance\n")
    for i in range(len(dist)):
        print("  ",i,"\t",dist[i])


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = []
for i in range(e):
    graph.append(list(map(int, input("Enter u,v,w: ").split())))
src= int(input("Enter source: "))
bellman(graph,src, n)