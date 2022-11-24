#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        sum = 0
        # last1:表示上一次属于[left,right]的数字出现的位置，如果不存在则为-1
        # last2:表示上一次大于right数字出现的位置，如果不存在则为-1。
        last1 = last2 = -1
        for i, x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            if last1 != -1:
                sum += last1 - last2        
        return sum
            
# @lc code=end

