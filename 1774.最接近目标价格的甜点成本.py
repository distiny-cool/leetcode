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

"""官方题解使用DFS+回溯
   理论上这样确实会更快一点，毕竟后面的都不用算，我自己的太暴力了
   但实际上我的运行时间要更短，一方面是set()的功劳，另一方面递归调用确实费时
   以前学数据结构的时候养成了喜欢迭代的习惯，感觉这种东西都可以改成一个栈，，，但是现在又懒hhhh
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = min(baseCosts)
        def dfs(p: int, cur_cost: int) -> None:
            nonlocal ans
            if abs(ans - target) < cur_cost - target:
                return
            if abs(ans - target) >= abs(cur_cost - target):
                if abs(ans - target) > abs(cur_cost - target):
                    ans = cur_cost
                else:
                    ans = min(ans, cur_cost)
            if p == len(toppingCosts):
                return
            dfs(p + 1, cur_cost + toppingCosts[p] * 2)
            dfs(p + 1, cur_cost + toppingCosts[p])
            dfs(p + 1, cur_cost)
        for c in baseCosts:
            dfs(0, c)
        return ans
"""

# @lc code=end
