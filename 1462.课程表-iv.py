#
# @lc app=leetcode.cn id=1462 lang=python3
#
# [1462] 课程表 IV
#

# @lc code=start
# 寄，超时了
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         # 构建图
#         graph = [[] for _ in range(numCourses)]
#         for pre in prerequisites:
#             graph[pre[0]].append(pre[1])

#         # 搜索
#         def dfs(i,j):
#             if (j in graph[i]):
#                 return 1
#             ret = 0
#             for n in graph[i]:
#                 ret += dfs(n,j)
#             return ret
        
#         # 遍历
#         ans = []
#         for q in queries:
#             ans.append(dfs(q[0],q[1])>0)
#         return ans

# 用floyd算法
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # 构建一个二维数组图，用于表示课程之间的依赖关系
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for pre in prerequisites:
            # 如果课程 pre[0] 依赖于课程 pre[1]，则将对应的图中位置标记为1
            graph[pre[0]][pre[1]] = 1

        # 使用 Floyd 算法来更新图，以找出所有课程之间的传递性依赖关系
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # 如果课程 i 依赖于课程 k 且课程 k 依赖于课程 j，则课程 i 依赖于课程 j
                    if (graph[i][k] and graph[k][j]):
                        graph[i][j] = 1
        
        # 遍历查询列表，检查每对课程是否有依赖关系，将结果添加到答案列表中
        ans = []
        for q in queries:
            # 如果课程 q[0] 依赖于课程 q[1]，则添加 True，否则添加 False
            ans.append(graph[q[0]][q[1]] == 1)
        return ans
# @lc code=end
