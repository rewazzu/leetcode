# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def swap(root):
    if root.left:
        swap(root.left)
    if root.right:
        swap(root.right)
    root.left, root.right = root.right, root.left
    return


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            swap(root)
        return root


'''Commentary: Simple Recursive invert binary tree. '''