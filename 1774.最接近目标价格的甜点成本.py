#
# @lc app=leetcode.cn id=1774 lang=python3
#
# [1774] 最接近目标价格的甜点成本
#


# @lc code=start
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int],
                    target: int) -> int:
        allTopType = set([0])
        for topping in toppingCosts:
            newTop = set()
            for i in allTopType:
                newTop.add(i + topping)
                newTop.add(i + topping * 2)
            allTopType |= newTop
        dist = 10**4
        for base in baseCosts:
            for i in allTopType:
                newdist = base + i - target
                if abs(newdist)<=abs(dist):
                    if abs(newdist)<abs(dist):
                        dist = newdist
                    else: dist = min(dist,newdist)
        return target+dist           

# @lc code=end
