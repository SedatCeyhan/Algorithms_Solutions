def makeConnected(n, connections):
    if len(connections) < n - 1: return -1
    G = [set() for i in range(n)]
    for i, j in connections:
        G[i].add(j)
        G[j].add(i)
    seen = [0] * n

    def dfs(i):
        if seen[i]: return 0
        seen[i] = 1
        for j in G[i]: dfs(j)
        return 1

    return sum(dfs(i) for i in range(n)) - 1

def makeConnected2(n, comp_from, comp_to):
    if len(comp_from) < n - 1: return -1
    graph = [set() for i in range(n)]
    for i in range(len(comp_from)):
        graph[comp_from[i]].add(comp_to[i])
        graph[comp_to[i]].add(comp_from[i])
    seen = [0] * n

    def dfs(i):
        if seen[i]: return 0
        seen[i] = 1
        for j in graph[i]: dfs(j)
        return 1

    return sum(dfs(i) for i in range(n)) - 1


print(makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
print(makeConnected2(6, [0,0,0,1], [1,2,3,2]))

