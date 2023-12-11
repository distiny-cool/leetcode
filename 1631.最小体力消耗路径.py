#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 使用Dijkstra算法
        # 1. 初始化
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        seen = [[0] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        # 2. 迭代
        while pq:
            d, x, y = heapq.heappop(pq)
            if seen[x][y]:
                continue
            seen[x][y] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = max(d, abs(heights[x][y] - heights[nx][ny]))
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))
        return dist[-1][-1]
    
# @lc code=end

