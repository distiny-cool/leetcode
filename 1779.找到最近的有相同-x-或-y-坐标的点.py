#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dmin = 10**4
        ans = -1
        for n,(i,j) in enumerate(points):
            dx = abs(x-i)
            dy = abs(y-j)
            if(dx == 0):
                if(dy < dmin):
                    dmin = dy
                    ans = n
                continue
            if(dy == 0):
                if(dx < dmin):
                    dmin = dx
                    ans = n
            
        return ans
# @lc code=end

