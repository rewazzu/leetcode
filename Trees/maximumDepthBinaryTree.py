def dfs(root):
    left_depth = 1
    right_depth = 1
    if root.left:
        left_depth = dfs(root.left) + 1
    if root.right:
        right_depth = dfs(root.right) +1
    return max(left_depth, right_depth)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = dfs(root)
        return depth


'''Commentary: Simple DFS runs in O(n) time'''