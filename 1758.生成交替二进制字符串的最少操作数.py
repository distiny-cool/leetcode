#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        way1 = way2 = flag = 0
        for i in range(len(s)):
            if (int(s[i])+flag)%2:
                way1 += 1
            else:
                way2 += 1
            flag = not flag
        return min(way1,way2)
# @lc code=end

