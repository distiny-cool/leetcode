#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(i)-ord("a")+1) for i in s)
        s = map(int,s)
        for _ in range(k-1):
            s = list(map(int, str(sum(s))))
        return sum(s)
# @lc code=end

