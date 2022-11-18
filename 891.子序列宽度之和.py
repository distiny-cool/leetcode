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
        d = list()
        for i in range(1,len(nums)):
            d.append(nums[i]-nums[i-1])
        k = 1
        DistAsMax = [0 for _ in range(len(d))]
        DistAsMax[0] = d[0]
        for i in range(1,len(d)):
            DistAsMax[i] = (2*(DistAsMax[i-1]+k*d[i])+d[i])
            k = 2*k + 1
        return sum(DistAsMax)%MOD

# @lc code=end

