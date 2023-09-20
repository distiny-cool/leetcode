# 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。
# 我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

class Solution:
    def minCount(self, coins: List[int]) -> int:
        # return sum(i/2+1 if i%2 else i/2 for i in coins)
        return sum(c // 2 + c % 2 for c in coins)