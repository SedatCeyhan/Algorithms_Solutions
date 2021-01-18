from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        if n == 0 or not edges: return n
        discovered, graph = defaultdict(lambda: False), defaultdict(list)
        components = 0

        def formGraph(edges):
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

        def dfs(n):
            discovered[n] = True
            for nbr in graph[n]:
                if not discovered[nbr]:
                    dfs(nbr)

        formGraph(edges)
        for node in range(n):
            if not discovered[node]:
                dfs(node)
                components += 1

        return components



    def listOfComponents(self, n, edges):
        if n == 0 or not edges: return n

        discovered, graph = defaultdict(lambda: False), defaultdict(list)
        components = []

        def formGraph(edges):
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

        def dfs(n, comps):
            discovered[n] = True
            comps.append(n)
            for nbr in graph[n]:
                if not discovered[nbr]:
                    dfs(nbr, comps)

        formGraph(edges)
        for node in range(n):
            comps = []
            if not discovered[node]:
                dfs(node, comps)
                components.append(comps)


        return components


sol = Solution()
print(sol.listOfComponents(5, [[0, 1], [1, 2], [3, 4]]))
