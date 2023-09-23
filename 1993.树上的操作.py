#
# @lc app=leetcode.cn id=1993 lang=python3
#
# [1993] 树上的操作
#

# @lc code=start

class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locked = [-1]*n
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for i in range(n):
            if parent[i] != -1:
                self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False
    
    def hasLockedChild(self, num:int) -> bool:
        res = False
        for child in self.children[num]:
            if self.locked[child] != -1:
                self.locked[child] = -1
                res = True
            res |= self.hasLockedChild(child)
        return res

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        
        par = self.parent[num]
        while(par != -1):
            if self.locked[par] != -1:
                return False
            par = self.parent[par]

        if self.hasLockedChild(num):
            self.locked[num] = user
            return True
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
            
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# @lc code=end