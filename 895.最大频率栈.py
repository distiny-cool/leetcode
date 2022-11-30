#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.fre = defaultdict(int)
        self.group = defaultdict(list)
        self.max_fre = 0

    def push(self, val: int) -> None:
        self.fre[val] += 1
        self.group[self.fre[val]].append(val)
        self.max_fre = max(self.max_fre, self.fre[val])

    def pop(self) -> int:
        val = self.group[self.max_fre].pop()
        self.fre[val] -= 1
        if(len(self.group[self.max_fre])==0):
            self.max_fre -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

