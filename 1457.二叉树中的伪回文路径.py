#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
#

# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, path):
            nonlocal ans
            if not root:
                return
            path ^= 1 << root.val
            if not root.left and not root.right:
                if path & (path - 1) == 0:
                    ans += 1
                return
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, 0)
        return ans
# @lc code=end

