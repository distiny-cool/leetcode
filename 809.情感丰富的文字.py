# @before-stub-for-debug-begin
from python3problem809 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=809 lang=python3
#
# [809] 情感丰富的文字
#

# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        sum = 0
        for word in words:
            i = j = 1
            if word[0] != s[0]:
                continue
            flag = False
            while(i < len(s) and j < len(word)):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                    continue
                elif s[i-1]==s[i]==s[i+1] or (i > 1 and s[i]==s[i-2]==word[j-1]):
                    flag = True
                    i += 1
                    while(i < len(s) and s[i-1]==s[i]):
                        i += 1
                else:
                    flag = False
                    break
            if(flag and j==len(word)): sum += 1
        return sum


# @lc code=end

