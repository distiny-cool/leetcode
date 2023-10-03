#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
# 对于此类的动态规划题目
# 最原始的方法就是想清楚到达每个点的所有情况
# 然后把这些情况的结果都算出来，在一步一步往下走
# 就绝对不会出错
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        end = len(prices)
        ans = [[-10**5-1]*4 for _ in range(end)]
        # ans[i][0] 首次买入
        # ans[i][1] 首次卖出
        # ans[i][2] 二次买入
        # ans[i][3] 二次卖出
        ans [0][0] = -prices[0]
        max_money = 0
        for i in range(1,end):
            ans[i][0] = max(ans[i-1][0],-prices[i])
            ans[i][1] = max(ans[i-1][1],ans[i-1][0]+prices[i])
            ans[i][2] = max(ans[i-1][2],ans[i-1][1]-prices[i])
            ans[i][3] = max(ans[i-1][3],ans[i-1][2]+prices[i])
            max_money = max(max_money,ans[i][1],ans[i][3])
        return max_money

# @lc code=end

