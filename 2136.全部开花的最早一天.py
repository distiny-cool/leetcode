#
# @lc app=leetcode.cn id=2136 lang=python3
#
# [2136] 全部开花的最早一天
#

# @lc code=start
# 先种下growTime长的花就行
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant,grow = 0,0
        for grow_i,plant_i in sorted(zip(growTime,plantTime),reverse=True):
            plant += plant_i
            grow = max(grow,plant + grow_i)
        return grow
# @lc code=end

