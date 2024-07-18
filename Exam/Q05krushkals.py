#5 Greedy  O(ElogE)
def find(parent, i):
    if parent[i]==i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)

    if rank[rx]<rank[ry]:
        parent[rx]=ry
    elif rank[rx]>rank[ry]:
        parent[ry]=rx
    else:
        parent[ry]=rx
        rank[rx]+=1

def krushkals(graph, V):
    e = 0
    parent = list(range(V))
    rank = [0]*V
    graph.sort(key = lambda item:item[2])
    res = []
    while e<V-1:
        u,v,w = graph[e]
        x = find(parent, u)
        y = find(parent, v)
        if x!=y:
            e+=1
            res.append([u,v,w])
            union(parent, rank, x,y)
    return res

def take_input():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    graph = []
    print("Enter edges in the format 'u v w' (space separated), where u, v are vertices and w is weight:")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph.append([u, v, w])
    return graph, vertices

graph, vertices = take_input()
mst = krushkals(graph, vertices)
print("Minimum Spanning Tree (u, v, weight):", mst)