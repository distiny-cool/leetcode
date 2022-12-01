from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = r = 0
        ans = [0]*len(boxes)
        for i,box in enumerate(boxes):
            if box == '1':
                r += 1
                ans[0] += i
        for i in range(1,len(boxes)):
            if boxes[i-1] == '1':
                r -= 1
                l += 1
            ans[i] = ans[i-1] + l - r
        return ans

a = Solution()
print(a.minOperations("010101111011"))