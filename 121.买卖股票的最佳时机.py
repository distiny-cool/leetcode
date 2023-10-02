#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        count = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                count += prices[i] - prices[i-1]
        return count


# @lc code=end

