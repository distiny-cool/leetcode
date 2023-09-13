#
# @lc app=leetcode.cn id=2596 lang=python3
#
# [2596] 检查骑士巡视方案
#
# @lc code=start
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        times = 0
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]  # 所有可能的移动方向

        def CanOrNot(i, j, times):
            if times == n * n - 1:
                return True
            pre = grid[i][j]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == pre + 1:
                    times += 1
                    return CanOrNot(ni, nj, times)
            return False

        i = j = 0
        return CanOrNot(i, j, times)
# @lc code=end

# def checkValidGrid(self, grid: List[List[int]]) -> bool:
#         n = len(grid)
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     if i - 2 >= 0 and j - 1 >= 0 and grid[i-2][j-1] == 1:
#                         return False
#                     if i - 2 >= 0 and j + 1 < n and grid[i-2][j+1] == 1:
#                         return False
#                     if i - 1 >= 0 and j - 2 >= 0 and grid[i-1][j-2] == 1:
#                         return False
#                     if i - 1 >= 0 and j + 2 < n and grid[i-1][j+2] == 1:
#                         return False
#         return True
