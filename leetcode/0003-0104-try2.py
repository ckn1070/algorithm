# Solved
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(nodes):
            if nodes is None:
                return 0

            return 1 + max(dfs(nodes.left), dfs(nodes.right))

        return dfs(root)
