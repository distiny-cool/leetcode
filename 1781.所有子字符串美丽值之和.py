#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#

# @lc code=start
from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        ans, n = 0, len(s)
        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1                     
                ans += max(freq.values()) - min(freq.values())
        return ans
        

# @lc code=end
"""暴力解法最后一个超时。。。
class Solution:
    def beautySum(self, s: str) -> int:
        def beautyValue(s:str) -> int:
            freq = Counter(s)
            return max(freq.values()) - min(freq.values())
        ans = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                ans += beautyValue(s[i:j])
        return ans
"""