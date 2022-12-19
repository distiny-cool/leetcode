#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
# 抄的答案
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        vis = {source}
        queue = deque([source])
        e = defaultdict(set)
        for u,v in edges:
            e[u].add(v)
            e[v].add(u)
        while queue:
            cur = queue.popleft()
            if cur == destination:
                return True
            for nxt in e[cur]:
                if nxt not in vis:
                    vis.add(nxt)
                    queue.append(nxt)
        return False
# @lc code=end

