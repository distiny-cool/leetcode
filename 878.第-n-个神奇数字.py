# @before-stub-for-debug-begin
from math import gcd, lcm
from python3problem878 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

# @lc code=start

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        g=lcm(a,b)
        l=min(a,b)
        r=n*l
        while l<=r:
            mid=(l+r)//2
            if mid//a+mid//b-mid//g>=n:
                cur=mid
                r=mid-1
            else:
                l=mid+1
        return cur%(10**9+7)

# @lc code=end

