'''

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and
an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
Notice that you can return the vertices in any order

'''


class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        innerNodes = []
        for e in edges:
            innerNodes.append(e[1])

        return list(set(range(n)) - set(innerNodes))

sol = Solution()
print(sol.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))

