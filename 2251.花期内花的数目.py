#
# @lc app=leetcode.cn id=2251 lang=python3
#
# [2251] 花期内花的数目
#

# @lc code=start

# 我知道肯定会超时
# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
#         ans = [0]*len(people)
#         for i in range(len(people)):
#             for j in flowers:
#                 if j[0]<=people[i]<=j[1]:
#                     ans[i] += 1
#         return ans

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        change = collections.defaultdict(int)
        for start,end in flowers:
            change[start] += 1
            change[end+1] -= 1
        change = sorted(change.items())
        len_people = len(people)
        sorted_people = sorted(zip(people,range(len_people)))
        ans = [0]*len_people
        i,curr = 0,0
        for j,n in sorted_people:
            while i < len(change) and change[i][0] <= j :
                curr += change[i][1]
                i += 1
            ans[n] = curr
        return ans

# 二分法
class Solution2:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]
        
# @lc code=end
