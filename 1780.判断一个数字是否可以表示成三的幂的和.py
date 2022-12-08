#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 如果n为3的幂，则返回True
        if math.log(n, 3).is_integer():
            return True
    
        # 如果n不为3的幂，则将n分解为多个3的幂的和
        powers = []
        power = 0
        while 3**power <= n:
            powers.append(3**power)
            power += 1
        powers = sorted(powers, reverse=True)
    
        # 使用从大到小的3的幂来减少n的值
        for p in powers:
            if n - p == 0:
                # 如果减少后n为0，则返回True
                return True
            elif n - p > 0:
                # 如果减少后n大于0，则继续尝试使用更小的3的幂减少n的值
                n -= p
    
        # 如果无法减少n的值，则返回False
        return False     
# @lc code=end

