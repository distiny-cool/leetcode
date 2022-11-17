# @before-stub-for-debug-begin
from collections import defaultdict, deque
from python3problem792 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#

# @lc code=start

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = len(words)
        words = Counter(words)
        for word in words:
            i = 0
            for c in word:
                i = s.find(c, i) + 1
                if not i:
                    ans -= words[word]
                    break
        return ans

# @lc code=end

"""莫名其妙，感觉自己方法没问题（虽然不够好，但懒得改了），结果有10个没过
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ds = defaultdict(list)
        for i,c in enumerate(s):
            if c in ds:
                ds[c].append(i)
            else:
                ds[c].append(1) # ds[c][0]用来动态表示匹配过程中该字母剩下首个的位置
                ds[c].append(i)
        
        def MatchWord(ds,word):
            idx = -1
            for c in word:
                if c in ds:
                    flag = 0
                    while ds[c][0] < len(ds[c]):
                        if ds[c][ds[c][0]] > idx:
                            idx = ds[c][ds[c][0]]
                            flag = 1
                            break
                        ds[c][0] += 1
                    if flag: continue
                    return False
                else: return False
            return True
        
        sum = 0
        for word in words:
            if len(word) > len(s):
                continue
            if MatchWord(ds,word):
                sum += 1
                for c in ds:
                    ds[c][0] = 1
        
        return sum
"""      
        
"""暴力解法会超时
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def Match(s:str,word:str) -> bool:
            lenth = len(word)
            k = 0
            for i in s:
                if i == word[k]:
                    k += 1
                    if k == lenth:
                        return True
            return False
        
        return sum(Match(s,word) for word in words)
"""

