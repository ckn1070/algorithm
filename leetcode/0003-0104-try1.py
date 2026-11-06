# NOT Solved
# TreeNode라는 외부 클래스가 따로 정의되어있는 형태를 아예 처음 접해본다
# Try 2
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

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


# Try 1
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def rec(self, nodes, depth):
#         if 2**depth <= len(nodes):
#             return True
#         return False
#
#     def maxDepth(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#
#         depth = 0
#         while True:
#             if not self.rec(root[2**depth:], depth):
#                 break
#
#             depth += 1
#
#         return depth + 1
#
# sol = Solution()
# print(sol.maxDepth([3,9,20,None,None,15,7]))
# print(sol.maxDepth([1,None,2]))