#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def soup(m,n):
            if m <=0 and n <= 0:
                return 0.5
            if m <= 0:
                return 1
            if n <= 0:
                return 0
            return 0.25*(soup(m-100,n)+soup(m-50,n-50)+soup(m-75,n-25)+soup(m-25,n-75))
        return 1 if n > 4800 else soup(n,n)
# @lc code=end

