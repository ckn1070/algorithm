# Solved (간신히..)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        leaf1, leaf2 = [], []

        def leafSearch(root, leaf):
            if not root:
                return

            if root.right or root.left:
                leafSearch(root.right, leaf)
                leafSearch(root.left, leaf)
            else:
                leaf.append(root.val)


        leafSearch(root1, leaf1)
        leafSearch(root2, leaf2)
        print(leaf1, leaf2)

        if len(leaf1) != len(leaf2):
            return False

        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True


# GPT
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         def get_leaves(root):
#             leaves = []
#
#             def dfs(node):
#                 if node is None:
#                     return
#
#                 if node.left is None and node.right is None:
#                     leaves.append(node.val)
#                     return
#
#                 dfs(node.left)
#                 dfs(node.right)
#
#             dfs(root)
#             return leaves
#
#         return get_leaves(root1) == get_leaves(root2)