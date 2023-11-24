#
# @lc app=leetcode.cn id=2316 lang=python3
#
# [2316] 统计无向图中无法互相到达点对数
#

# @lc code=start
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans = n*(n-1)//2
        mmap = {}
        connect = [set([i]) for i in range(n)]
        
        for i in range(n):
            mmap[i] = i
        
        for edge in edges:
            if mmap[edge[1]] != mmap[edge[0]]:
                to = min(edge)
                fm = max(edge)
                ans -= len(connect[mmap[to]])*len(connect[mmap[fm]])
                connect[mmap[to]] |= connect[mmap[fm]]
                
                for node in connect[mmap[fm]]:
                    mmap[node] = mmap[to]
        
        return ans
        
# @lc code=end

