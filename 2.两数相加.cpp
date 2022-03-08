/*
 * @Descripttion:
 * @version:
 * @Author: distiny
 * @Date: 2022-03-08 18:44:33
 * @LastEditors: distiny
 * @LastEditTime: 2022-03-08 20:25:14
 */
/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start

// Definition for singly-linked list.
// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *ans = nullptr;
        ListNode *tail = nullptr, *head = nullptr;
        int temp;
        bool flag = false;
        while (l1)
        {
            if (l2)
            {
                temp = l1->val + l2->val;
                l2 = l2->next;
                temp = flag ? temp + 1 : temp;
            }
            else
                temp = flag ? l1->val + 1 : l1->val;

            l1 = l1->next;

            if (temp >= 10)
            {
                flag = true;
                if (ans == nullptr)
                {
                    ans = new ListNode(temp - 10);
                    head = ans;
                }
                else
                {
                    tail = new ListNode(temp - 10);
                    head->next = tail;
                    head = head->next;
                    tail = tail->next;
                }
            }
            else
            {
                flag = false;
                if (ans == nullptr)
                {
                    ans = new ListNode(temp);
                    head = ans;
                }
                else
                {
                    tail = new ListNode(temp);
                    head->next = tail;
                    head = head->next;
                    tail = tail->next;
                }
            }
        }
        while (l2)
        {
            temp = flag ? l2->val + 1 : l2->val;
            if (temp >= 10)
            {
                flag = true;
                temp = temp - 10;
            }
            else
                flag = false;
            tail = new ListNode(temp);
            head->next = tail;
            head = head->next;
            tail = tail->next;
            l2 = l2->next;
        }
        if (flag)
        {
            tail = new ListNode(1);
            head->next = tail;
            head = head->next;
        }

        return ans;
    }
};
// @lc code=end
