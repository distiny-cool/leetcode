# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        n = numRows         # 行数
        if n == 1:          # 行数为1，直接返回
            return s

        res = [''] * n      # 记录结果，数组长度为n，其中res[i]表示第i行的字符（0<=i<=n-1）
        
        sign = -1           # Z字形行走的方向（+1表示向下走，-1表示向上走）
        i = 0               # 初始时在第一行
        for ch in s:
            res[i] += ch
            if i == 0 or i == n-1:      # 在第一行和最后一行转向
                sign = -sign            # Z字形行走反转方向
            i += sign                   # 下一行（向下+1，向上-1）
        
        return ''.join(res)     # res[i]表示第i行的字符，累加即可得最终结果

# @lc code=end

