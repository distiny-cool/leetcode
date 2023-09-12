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

        # 构建图
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for pre in prerequisites:
            graph[pre[0]][pre[1]] = 1

        # floyd算法
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if (graph[i][k] and graph[k][j]):
                        graph[i][j] = 1
        
        # 遍历
        ans = []
        for q in queries:
            ans.append(graph[q[0]][q[1]]==1)
        return ans
# @lc code=end
