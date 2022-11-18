# @before-stub-for-debug-begin
from python3problem891 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

# @lc code=start


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        if(len(nums)==1):
            return 0
        for i in range(0,len(nums)-1):
            nums[i] = nums[i+1]-nums[i]
        k = 1
        DistAsMax = [0 for _ in range(len(nums)-1)]
        DistAsMax[0] = nums[0]
        for i in range(1,len(nums)-1):
            DistAsMax[i] = (2*(DistAsMax[i-1]+k*nums[i])+nums[i])
            k = 2*k + 1
        return sum(DistAsMax)%MOD
        
"""官方题解
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7
        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % MOD
            x = (x * 2 + nums[j]) % MOD
            y = y * 2 % MOD
        return (res + MOD) % MOD
"""
# @lc code=end

