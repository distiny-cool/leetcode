# @before-stub-for-debug-begin
from python3problem790 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        """四种状态"""
        """0:空 1:上覆盖 2:下覆盖 3:铺满"""
        cur = [1,0,0,0] # 保存当前的这块瓷砖状态,初始状态为0
        for _ in range(0,n):
            next = [0,0,0,0] # 保存下一块瓷砖状态
            next[0] = (cur[0] + cur[3])%MOD
            next[1] = (cur[0] + cur[2])%MOD
            next[2] = (cur[0] + cur[1])%MOD
            next[3] = (cur[0] + cur[1] + cur[2])%MOD
            cur = next
        return cur[0]
# @lc code=end

