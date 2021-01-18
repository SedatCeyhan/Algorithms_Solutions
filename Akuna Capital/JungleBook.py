
class Solution:
    def __init__(self):
        self.Nodes = []
        self.Depth = []

    def DepthTracker(self, nodes):
        self.Nodes = nodes
        self.Depth = [0] * len(self.Nodes)

        for i in range(len(self.Nodes)):
            if self.Nodes[i] > -1 and self.Depth[i] == 0:
                self.Depth[i] = self.CheckDepth(i)

    def CheckDepth(self, index):
        if index == -1: return 0

        if self.Depth[index] > 0: return self.Depth[index]
        nextIdx = self.Nodes[index]
        if nextIdx == -1:
            self.Depth[index] = 0
            return 0

        thisDepth = self.CheckDepth(nextIdx) + 1
        self.Depth[index] = thisDepth
        return thisDepth

    def GetHeight(self):
        return max(self.Depth)

    def GetTreeHeight(self, nodes):
        self.DepthTracker(nodes)
        return self.GetHeight() + 1

#
# def DepthTracker(nodes):
#     Nodes = nodes
#     Depth = [0] * len(Nodes)
#     print(Depth)
#     for i in range(len(Nodes)):
#         if Nodes[i] > -1 and Depth[i] == 0:
#             Depth[i] = CheckDepth(i)
#
# def CheckDepth(index):
#     if index == -1: return 0
#     print(Depth)
#     print(index)
#     if Depth[index] > 0: return Depth[index]
#     nextIdx = Nodes[index]
#     if nextIdx == -1:
#         Depth[index] = 0
#         return 0
#
#     thisDepth = CheckDepth(nextIdx) + 1
#     Depth[index] = thisDepth
#     return thisDepth
#
# def GetHeight():
#     return max(Depth)
#
# def GetTreeHeight(nodes):
#     DepthTracker(nodes)
#     #return GetHeight() + 1
#

sol = Solution()
print(sol.GetTreeHeight([3,2,4,-1,-1,8,-1,9,9,-1]))