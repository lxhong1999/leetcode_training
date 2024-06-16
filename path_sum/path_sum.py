# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        s = []
        
        def path(root,s1):
            if not root:
                return
            s1 = s1 + root.val
            if root.left == None and root.right == None:
                s.append(s1)
                return 

            if root.left:
                path(root.left,s1)
            if root.right:
                path(root.right,s1)
        path(root,0)
        
        return targetSum in s