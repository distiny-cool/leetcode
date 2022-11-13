#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
from collections import deque

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pri = dict()
        for i in order:
            pri[i]=''
        ans = ''

        for i in s:
            if i in pri:
                pri[i] += i
            else:
                ans += i

        for i in order:
            ans += pri[i]

        return ans 

# @lc code=end

