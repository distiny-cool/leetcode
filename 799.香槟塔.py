# @before-stub-for-debug-begin
from python3problem799 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [0] * 100
        tower[0] = poured
        for i in range(query_row):
            for j in range(min(i, query_glass), -1, -1):
                glass = tower[j]
                tower[j] = 0
                if glass > 1:
                    tower[j+1] += (glass-1)/2
                    tower[j] += (glass-1)/2
        return min(1, tower[query_glass])

# @lc code=end

