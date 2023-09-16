#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        ans = [0 for _ in range(length + 1)]
        ans[0] = 0
        ans[1] = nums[0]
        for i in range(2, length + 1):
            ans[i] = max(ans[i - 2] + nums[i - 1], ans[i - 1])
        return ans[length]
# @lc code=end
