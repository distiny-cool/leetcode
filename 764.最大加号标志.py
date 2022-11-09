# @before-stub-for-debug-begin
from python3problem764 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#

# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        ans = 0
        dp = [[0] * n for _ in range(n)]
        for i, j in mines:
            dp[i][j] = -1
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if dp[i][j] == -1:
                    count = 0
                else:
                    count += 1
                    dp[i][j] = count
            count = 0
            for j in range(n - 1, -1, -1):
                if dp[i][j] == -1:
                    count = 0
                else:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])

        for j in range(0, n):
            count = 0
            for i in range(0, n):
                if dp[i][j] == -1:
                    count = 0
                else:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])
            count = 0
            for i in range(n-1, -1, -1):
                if dp[i][j] == -1:
                    count = 0
                else:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])
                ans = max(ans,dp[i][j])
        return ans


# @lc code=end
