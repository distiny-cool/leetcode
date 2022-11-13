# @before-stub-for-debug-begin
from math import gcd
from python3problem805 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """转化成一个平均数为0的list"""
        n, s = len(nums), sum(nums)
        mul = n//gcd(n, s)
        A = [num*mul-mul*s//n for num in nums]
        """算出当部分数值之和为0时，则可以均值分割"""
        res = set()
        for x in A[:-1]:
            res |= {sub+x for sub in res|{0}}
            if 0 in res:
                return True
        return False
# @lc code=end

