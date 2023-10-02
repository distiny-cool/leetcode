#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,count,cur_min = 0,0,10**4+1
        end = len(prices)
        while i<end:
            if prices[i] <= cur_min:
                cur_min = prices[i]
                i += 1
                continue
            if i == end - 1:
                count += prices[i] - cur_min
                break
            if prices[i+1] < prices[i]:
                count += prices[i] - cur_min
                cur_min =  prices[i+1]
                i += 2
            else:
                i += 1
        return count
# @lc code=end

