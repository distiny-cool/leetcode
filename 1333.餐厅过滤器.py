#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#

# @lc code=start
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        i = 0
        while i < len(restaurants):
            if veganFriendly:
                if restaurants[i][2]==0:
                    del(restaurants[i])
                    continue
            if restaurants[i][3] > maxPrice or restaurants[i][4] > maxDistance:
                del(restaurants[i])
                continue
            i += 1
        restaurants.sort(key=lambda x:(x[1],x[0]),reverse=True)
        return [rest[0] for rest in restaurants]
            
# @lc code=end

