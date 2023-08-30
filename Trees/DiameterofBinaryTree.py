# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        left_tree = 0
        right_tree = 0
        left_best = 0
        right_best = 0

        if root.left:
            left_tree, left_best = self.dfs(root.left)
            left_tree += 1
        if root.right:
            right_tree, right_best = self.dfs(root.right)
            right_tree += 1

        depth = max(left_tree, right_tree)
        best = max(left_tree + right_tree, right_best, left_best)
        return depth, best

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length, best = self.dfs(root)
        return best

'''
Commentary:
The trick here is to recognize that the diameter when the left_depth + right_depth is maximized.
Each level can only use the maximum of the deeper levels left depth or right depth
This runs in O(n) time
'''