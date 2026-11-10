# NOT Solved
#
# 으으.. 진짜 개간단해보이는데 이걸 대체 왜 못푸는거지?
#
# prefix를 두는 것은 뭔가 DP같은 느낌이랄까..
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# GPT
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, current):
            if node is None:
                return 0

            current += node.val

            count = prefix[current - targetSum]

            prefix[current] += 1

            count += dfs(node.left, current)
            count += dfs(node.right, current)

            prefix[current] -= 1

            return count

        return dfs(root, 0)


# GPT - Try 개선
# class Solution:
#     def pathSum(self, root, targetSum):
#         answer = 0
#
#         def dfs(nodes, partSum):
#             nonlocal answer
#
#             if nodes is None:
#                 return
#
#             partSum += nodes.val
#
#             if partSum == targetSum:
#                 answer += 1
#
#             dfs(nodes.left, partSum)
#             dfs(nodes.right, partSum)
#
#         def route(nodes):
#             if nodes is None:
#                 return
#
#             dfs(nodes, 0)
#
#             route(nodes.left)
#             route(nodes.right)
#
#         route(root)
#         return answer


# Try 2
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        answer = 0
        def dfs(nodes, part):
            nonlocal answer
            if nodes is None:
                return

            part += nodes.val
            if part == targetSum:
                answer += 1

            dfs(nodes.left, part)
            dfs(nodes.right, part)

        def route(nodes):
            if nodes is None:
                return

            dfs(nodes,0)

            route(nodes.left)
            route(nodes.right)

        route(root)
        return answer



# Try 1
# class Solution(object):
#     def pathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: int
#         """
#
#         answer = 0
#         def dfs(nodes, partSum):
#             nonlocal answer
#             if partSum == targetSum:
#                 print(nodes, partSum)
#                 return 1
#
#             if nodes is None:
#                 return 0
#
#             if nodes.left is not None:
#                 answer += dfs(nodes.left, partSum + nodes.val)
#             if nodes.right is not None:
#                 answer += dfs(nodes.right, partSum + nodes.val)
#             return 0
#
#         def route(nodes):
#             nonlocal answer
#             if nodes is None:
#                 return 0
#
#             dfs(nodes, 0)
#
#             if nodes.left is not None:
#                 route(nodes.left)
#
#             if nodes.right is not None:
#                 route(nodes.right)
#
#             return 0
#
#         route(root)
#         return answer
