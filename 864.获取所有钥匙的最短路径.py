# @before-stub-for-debug-begin
from python3problem864 import *
from typing import *
from collections import deque

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=864 lang=python3
#
# [864] 获取所有钥匙的最短路径
#

# @lc code=start


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 表示方向

        m, n = len(grid), len(grid[0])
        sx = sy = 0  # 开始位置
        key_to_idx = dict()

        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    idx = len(key_to_idx)
                    key_to_idx[grid[i][j]] = idx
                elif grid[i][j] == "@":
                    sx, sy = i, j

        key_num = len(key_to_idx)
        q = deque([(sx, sy, 0)])  # 队列中sx和sy表示位置，第三位表示curr_keys的情况
        dist = dict()
        dist[(sx, sy, 0)] = 0

        while q:
            x, y, curr_keys = q.popleft()  # curr_keys表示当前收集钥匙情况(1有0无),curr_keys == 1<<key_num-1时表示找到了所有钥匙
            for tx, ty in dirs:
                nx, ny = x + tx, y + ty
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    if grid[nx][ny] == "." or (nx, ny) == (sx, sy):
                        if (nx, ny, curr_keys) not in dist:
                            dist[(nx, ny, curr_keys)] = dist[(x, y, curr_keys)] + 1
                            q.append((nx, ny, curr_keys))
                        """为什么不用考虑原来的dist[(nx,ny,collect)]的值比新的值大呢？--因为是广度优先呀！"""
                    elif grid[nx][ny].islower():
                        idx = 1 << key_to_idx[grid[nx][ny]]
                        if curr_keys & idx == 0:
                            new_collect = idx | curr_keys
                            if new_collect == (1 << key_num) - 1:
                                return dist[(x, y, curr_keys)] + 1
                        """注意：curr_keys会改变的，要考虑钥匙虽然已经拿到了，但是现在的curr_keys已经更新了的情况！"""
                        if (nx, ny, idx | curr_keys) not in dist:
                            dist[(nx, ny, idx | curr_keys)] = (
                                dist[(x, y, curr_keys)] + 1
                            )
                            q.append((nx, ny, idx | curr_keys))
                    else:
                        idx = 1 << key_to_idx[grid[nx][ny].lower()]
                        if curr_keys & idx:
                            if (nx, ny, curr_keys) not in dist:
                                dist[(nx, ny, curr_keys)] = dist[(x, y, curr_keys)] + 1
                                q.append((nx, ny, curr_keys))

        return -1


# @lc code=end
