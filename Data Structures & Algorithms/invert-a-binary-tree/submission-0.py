# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #logic here invert the left and right and tell the children to do the same
        #if you encounter a node with no children then return none
        if not root:
            return None
        #swapping
        root.left,root.right=root.right,root.left
        #calling the invert function on the children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        