# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if the both trees are empty, then we return true
        if not p and not q:
            return True
        #if there is a node mismatch or if p or q is empty
        if (not p or not q) or (p.val!=q.val):
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
