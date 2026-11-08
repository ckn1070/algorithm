# Solved - 풀긴 풀었는데 참 더럽게 풀었다
#
# 더해서 누적하는거는 중복이 많이 생길 것 같다
# 각 노드별로 Return을 뽑아내고, 그걸 더하는 방법이 있나..? 그럼 그 다음 노드로는 어떻게 넘어가지?
#
# 단순 리스트였으면 T/F 리스트라도 만들었을텐데
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Try 2
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(nodes, maximum):
            if not nodes:
                return 0

            cur = 1 if nodes.val >= maximum else 0

            maximum = max(maximum, nodes.val)

            left = dfs(nodes.left, maximum)
            right = dfs(nodes.right, maximum)

            return cur + left + right

        return dfs(root, -10**18)




# Me
# class Solution(object):
#     def goodNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#
#         def dfs(nodes, maximum, total):
#             if not nodes:
#                 return 0
#
#             if nodes.val >= maximum:
#                 maximum = nodes.val
#                 total.append(maximum)
#
#             return dfs(nodes.left, maximum, total) + dfs(nodes.right, maximum, total)
#
#         total = []
#         dfs(root, -10**18, total)
#         print(total)
#         return len(total)


# GPT
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, max_val):
#             if node is None:
#                 return 0
#
#             good = 1 if node.val >= max_val else 0
#
#             max_val = max(max_val, node.val)
#
#             left = dfs(node.left, max_val)
#             right = dfs(node.right, max_val)
#
#             return good + left + right
#
#         return dfs(root, root.val)