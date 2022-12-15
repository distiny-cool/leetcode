from typing import List
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        gap = abs(sum(nums)-goal)
        if gap%limit:
            return gap//limit + 1
        else:
            return gap//limit