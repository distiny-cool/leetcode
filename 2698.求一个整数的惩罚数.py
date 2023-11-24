ans = set()
def dfs(ixi, pos, total, i):
    if pos == len(ixi):
        if total == i:
            ans.add(i)
        return
    for j in range(pos, len(ixi)):
        dfs(ixi, j+1, total+int(ixi[pos:j+1]), i)
for i in range(10000):
    dfs(str(i*i), 0, 0, i)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(a**2 for a in range(1,n+1) if a in ans)