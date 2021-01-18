from collections import defaultdict

def largestConnectedComponent(relations):
    if not relations: return []

    for i in range(len(relations)):
        j = i + 1
        while j < len(relations) - 1:
            if len(list(set(relations[i]) & set(relations[j]))) > 0:
                relations[i].extend(relations[j])
                relations[i] = list(set(relations[i]))
                relations.remove(relations[j])
            else: j += 1

    return relations

print(largestConnectedComponent([['p1', 'p2', 'p3'], ['p5', 'p2'], ['p6', 'p7'], ['p8', 'p7']]))














class Solution:
    def countComponents(self, n, edges):
        discovered = {}
        for i in range(n):
            discovered[i] = 0
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(vertex):
            if discovered[vertex] == 0:
                discovered[vertex] = 1
                for neighbor in graph[vertex]:
                    dfs(neighbor)

        components = 0
        for v in range(n):
            if v not in graph: components += 1
            else:
                if discovered[v] == 0:
                    dfs(v)
                    components+=1
        return components



#print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
