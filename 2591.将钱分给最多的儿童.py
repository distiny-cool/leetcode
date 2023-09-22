#
# @lc app=leetcode.cn id=2591 lang=python3
#
# [2591] 将钱分给最多的儿童
#


# @lc code=start
# 解决这种问题：注意 上限，下限，特殊 即可！
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        i = money - children
        if i < 0:
            return -1
        if i > children * 7:
            return children - 1
        if i == 7 * children - 4:
            return children - 2
        return i // 7


# @lc code=end
