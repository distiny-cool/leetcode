/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        for (int i = 0; i < length; i++)
        {
            for (int j = i+1; j < length; j++)
            {
                if(nums[i]+nums[j]==target){
                    vector<int> ans;
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }
            }
            
        }
        vector<int> ans(0);
        return ans;
    }
};
// @lc code=end

