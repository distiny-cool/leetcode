#
# @lc app=leetcode.cn id=2582 lang=python3
#
# [2582] 递枕头
#


# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        last = time % (2 * n - 2)
        return last + 1 if last < n else 2 * n - last - 1


# @lc code=end
