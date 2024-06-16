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
        :rtype: List[List[int]]
        """

        ans = []
        if not root:
            return ans
        def dfs(node, s, a):
            if not node :
                return 
            s = s + node.val 
            a.append(node.val)
            if not node.left and not node.right:
                if s==targetSum:
                    ans.append(list(a))
                
            if node.left:
                dfs(node.left,s,a)
            if node.right:
                dfs(node.right,s,a)
            a.pop()

        dfs(root,0,[])
        return ans
        