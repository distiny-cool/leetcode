#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m].copy()
        i = j = t = 0
        while(i<m and j<n):
            if temp[i] < nums2[j]:
                nums1[t] = temp[i]
                i += 1
            else:
                nums1[t] = nums2[j]
                j += 1
            t += 1
        if j < n:
            nums1[t:] = nums2[j:]
        else:
            nums1[t:] = temp[i:]   

# @lc code=end

