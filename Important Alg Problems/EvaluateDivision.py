'''

You are given an array of variable pairs equations and an array of real numbers values, where
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

'''

from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        if not equations: return []
        n = len(equations)
        graph = defaultdict(list)

        def formGraph():
            for i in range(n):
                graph[equations[i][0]].append((equations[i][1], values[i]))
                graph[equations[i][1]].append((equations[i][0], 1/values[i]))

        def bfsQuery(x, y, discovered):
            queue = [(x, 1)]
            discovered[x] = True
            while queue:
                currNode, accumulated = queue.pop(0)
                for nbr in graph[currNode]:
                    if nbr[0] == y: return accumulated * nbr[1]
                    if not discovered[nbr[0]]:
                        discovered[nbr[0]] = True
                        queue.append((nbr[0], accumulated * nbr[1]))

            return -1

        formGraph()
        sol = []
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                sol.append(-1.0)
            elif query[0] == query[1]: sol.append(1.0)
            else:
                discovered = defaultdict(lambda: False)
                sol.append(bfsQuery(query[0], query[1], discovered))

        return sol


sol = Solution()

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(sol.calcEquation(equations, values, queries))