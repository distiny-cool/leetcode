#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = cur = 0
        for i in gain:
            cur += i
            ans = max(cur,ans)
        return ans
        
# @lc code=end

