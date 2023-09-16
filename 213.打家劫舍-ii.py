#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            i, j = 0, 0
            for num in nums:
                i = j
                j = max(j, i + num)
            return j
        return max(rob1(nums[:-1]), rob1(nums[1:])) if len(nums) != 1 else nums[0]

# @lc code=end
