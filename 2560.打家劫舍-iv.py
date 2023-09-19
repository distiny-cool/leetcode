#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#

# @lc code=start
# 没有仔细研究，需要重新搞懂
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(y : int) -> int:
            count, visited = 0, False
            for x in nums:
                if x <= y and not visited:
                    count, visited = count + 1, True
                else:
                    visited = False
            return count
        return bisect_left(range(min(nums), max(nums)), k, key = f) + min(nums)

# @lc code=end

