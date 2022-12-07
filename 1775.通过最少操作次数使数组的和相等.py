#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start

class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) > 6 * len(nums2):
            return -1
        if sum(nums1) < sum(nums2):
            nums1, nums2 = nums2, nums1
        sum1, sum2 = sum(nums1), sum(nums2)
        nums1.sort(reverse=True)
        nums2.sort()
        ans, i, j = 0, 0, 0
        while sum1 > sum2:
            ans += 1
            if j >= len(nums2) or nums1[i] - 1 > 6 - nums2[j]:
                sum1 -= nums1[i] - 1
                i += 1
            elif i >= len(nums1) or nums1[i] - 1 <= 6 - nums2[j]:
                sum2 += 6 - nums2[j]
                j += 1
        return ans

        
        
# @lc code=end

