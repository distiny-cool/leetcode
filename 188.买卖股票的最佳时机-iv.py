#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        buy = [-1001]*k
        sell = [0]*k
        for i in range(len(prices)):
            buy[0] = max(buy[0],-prices[i])
            sell[0] = max(sell[0],buy[0]+prices[i])
            for j in range(1,k):
                buy[j] = max(buy[j],sell[j-1]-prices[i])
                sell[j] = max(sell[j],buy[j]+prices[i])
        return sell[k-1]

# @lc code=end

