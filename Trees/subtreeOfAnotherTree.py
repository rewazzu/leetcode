# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def SameTree(root, subroot):
    if not root and not subroot:
        return True
    if root and not subroot:
        return False
    if not root and subroot:
        return False

    current_same = root.val == subroot.val
    left_same = SameTree(root.right, subroot.right)
    right_same = SameTree(root.left, subroot.left)
    return current_same and left_same and right_same


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if SameTree(root, subRoot):
            return True

        elif self.isSubtree(root.left, subRoot):
            return True
        elif self.isSubtree(root.right, subRoot):
            return True
        else:
            return False 