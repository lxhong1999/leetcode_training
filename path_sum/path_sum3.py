# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.ans = 0

        def dfs(node, start, s):
            if not node:
                return 
            s = s - node.val
            if s == 0:
                self.ans = self.ans + 1
            if node.left:
                dfs(node.left, False, s)
            if node.right:
                dfs(node.right, False, s)
            if start:
                if node.left:
                    dfs(node.left, True, targetSum)
                if node.right:
                    dfs(node.right, True, targetSum)
        dfs(root,True,targetSum)
        return self.ans