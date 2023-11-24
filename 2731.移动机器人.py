#
# @lc app=leetcode.cn id=2731 lang=python3
#
# [2731] 移动机器人
#
# @lc code=start

# 超时了。。。
class Solution2:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        rob = []
        for i in range(n):
            rob.append([nums[i],-1 if s[i]=='L' else 1])
        rob.sort()
        rob.append([3*10**9+1,1])
        for _ in range(d):
            i = 0
            while i<n:
                if rob[i][0]+rob[i][1] == rob[i+1][0]+rob[i+1][1]:
                    rob[i][0] = rob[i][0]+rob[i][1]
                    rob[i+1][0] = rob[i][0]
                    rob[i][1],rob[i+1][1] = rob[i+1][1],rob[i][1]
                    i += 2
                    continue
                if rob[i][0]+rob[i][1] > rob[i+1][0]+rob[i+1][1]:
                    rob[i][1],rob[i+1][1] = rob[i+1][1],rob[i][1]
                    if i>0 and rob[i-1][0] == rob[i][0]:
                        rob[i][1],rob[i-1][1] = 1,-1
                    i += 2
                    continue
                rob[i][0] = rob[i][0]+rob[i][1]
                if i>0 and rob[i-1][0] == rob[i][0]:
                    rob[i][1],rob[i-1][1] = 1,-1
                i += 1
        ans = 0
        for i in range(n-1):
            ans += (rob[i+1][0]-rob[i][0])*(i+1)*(n-1-i)
        return ans%(10**9+7)

# 官方题解
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        pos = [nums[i] - d if s[i] == 'L' else nums[i] + d for i in range(n)]
        pos.sort()
        return sum([(pos[i] - pos[i - 1]) * i * (n - i) for i in range(1, n)]) % mod

# @lc code=end

