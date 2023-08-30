class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        current_same = p.val == q.val

        return left_same and right_same and current_same


'''Commentary: This is a recursive DFS approach to the problem. O(p+q)  '''