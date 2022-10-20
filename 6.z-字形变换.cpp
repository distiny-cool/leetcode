// @before-stub-for-debug-begin
#include <vector>
#include <string>
// #include "commoncppproblem6.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Z 字形变换
 */

// @lc code=start
class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
            return s;

        int lenth = s.length();
        vector<string> vct(numRows);

        bool down = true;
        vct[0].push_back(s[0]);
        for (int i = 1; i < lenth; ++i)
        {
            if (down)
            {
                for (int j = 1; j < numRows && i < lenth; j++, i++)
                {
                    vct[j].push_back(s[i]);
                }
                down = false;
                i--;
            }
            else
            {
                for (int j = numRows - 2; j >= 0 && i < lenth; j--, i++)
                {
                    vct[j].push_back(s[i]);
                }
                down = true;
                i--;
            }
        }

        string ans;
        // for (int i; i < numRows; ++i)
        //     ans += vct[i];
        for (string str : vct)
            ans += str;

        return ans;
    }
};
// @lc code=end
