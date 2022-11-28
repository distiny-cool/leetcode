# @before-stub-for-debug-begin
import functools
from itertools import accumulate
from operator import add
# from python3problem813 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#

# @lc code=start


class Solution: #纯纯的暴力

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        @functools.lru_cache(maxsize=None)
        def largestSumOfAverages(i, n):  # 表示从i开始分n组的结果最大平均值和
            if i == lenth:
                return 0
            if n == 1:
                return (s[-1] - s[i]) / (lenth - i)
            ans = 0
            for j in range(i, lenth):
                t = (s[j + 1] - s[i]) / (j - i + 1) + largestSumOfAverages(
                    j + 1, n - 1)
                ans = max(ans, t)
            return ans

        lenth = len(nums)
        sum = 0.0
        s = [0.0]
        for i in range(len(nums)):  # 前缀和
            sum += nums[i]
            s.append(sum)
        return largestSumOfAverages(0, k)

# @lc code=end
