#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 可以攻击国王的皇后
#


# @lc code=start
# 我的做法：
# class Solution:
#     def queensAttacktheKing(
#         self, queens: List[List[int]], king: List[int]
#     ) -> List[List[int]]:
#         x0 = king[0]
#         y0 = king[1]
#         inians = [[-1,y0],[-1,9],[x0,9],[9,9],[9,y0],[9,-1],[x0,-1],[-1,-1]]
#         ans = inians.copy()
#         for x, y in queens:
#             if x > x0:
#                 if (y == x + y0 - x0) and (y > y0):
#                     if x - x0 < ans[3][0] - x0:
#                         ans[3] = [x, y]
#                     continue
#                 if y == y0:
#                     if x - x0 < ans[4][0] - x0:
#                         ans[4] = [x, y]
#                     continue
#                 if (y == x0 + y0 - x) and (y < y0):
#                     if x - x0 < ans[5][0] - x0:
#                         ans[5] = [x, y]
#                     continue
#                 continue
#             if x == x0:
#                 if (y > y0) and (ans[2][1] - y0 > y - y0):
#                     ans[2] = [x, y]
#                     continue
#                 if (y < y0) and (y0 - ans[6][1] > y0 - y):
#                     ans[6] = [x, y]
#                     continue
#                 continue
#             if x < x0:
#                 if y == y0:
#                     if x0 - x < x0 - ans[0][0]:
#                         ans[0] = [x, y]
#                     continue
#                 if (y < y0) and (y == x + y0 - x0):
#                     if x0 - x < x0 - ans[7][0]:
#                         ans[7] = [x, y]
#                     continue
#                 if (y > y0) and (y == x0 + y0 - x):
#                     if x0 - x < x0 - ans[1][0]:
#                         ans[1] = [x, y]
#                     continue
#                 continue
#         return [i for i in ans if i not in inians]

# 大佬的做法：
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(map(tuple, queens))
        ans = []
        for di, dj in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
            for i in range(8):
                q = king[0] + di * i, king[1] + dj * i
                if q in queens:
                    ans.append(q)
                    break
        return ans
# @lc code=end
