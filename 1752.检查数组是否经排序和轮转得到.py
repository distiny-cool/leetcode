#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        reverse = 0
        if nums[0] < nums[-1]:
            reverse += 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                reverse += 1
        if reverse > 1:
            return False
        else:
            return True
        

            
# @lc code=end

