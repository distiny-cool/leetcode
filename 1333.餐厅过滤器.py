#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#

# @lc code=start
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = [rest for rest in restaurants if rest[2]>=veganFriendly and rest[3]<=maxPrice and rest[4]<=maxDistance]
        ans.sort(key=lambda x:(x[1],x[0]),reverse=True)
        return [rest[0] for rest in ans]
            
# @lc code=end

