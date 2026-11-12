# Solved
#
# DFS를 사용하되, 레벨 추적하고 레벨별 가장 오른쪽 추가
#
# GPT - 같은 lv에서 for문을 돌려버리는 방법 (for문이 결국 하나의 lv)
#
# Definition for a binary tree node.
from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Try 2
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        answer = []
        visited = [False] * 100

        lv = 0
        q = deque([(root, 0)])
        while q:
            node, lv = q.popleft()

            if node is None:
                continue

            if not visited[lv]:
                visited[lv] = True
                answer.append(node.val)

            q.append((node.right, lv + 1))
            q.append((node.left, lv + 1))
            lv += 1

        print(answer)
        return answer


# GPT
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#
#         answer = []
#         q = deque([root])
#
#         while q:
#             size = len(q)
#
#             for i in range(size):
#                 node = q.popleft()
#
#                 if i == size - 1:
#                     answer.append(node.val)
#
#                 if node.left:
#                     q.append(node.left)
#
#                 if node.right:
#                     q.append(node.right)
#
#         return answer


# Try 1 - 너무 복잡한 로직으로 시도
# class Solution:
#     def rightSideView(self, root: TreeNode | None) -> list[int]:
#
#         answer = []
#
#         q = deque([(root, True)])
#         while q:
#             node, target = q.popleft()
#
#             if node is None:
#                 continue
#
#             if target:
#                 answer.append(node.val)
#
#             if node.right is not None and node.left is not None:
#                 print('both', node.right.val, node.left.val)
#                 q.append((node.right, True))
#                 q.append((node.left, False))
#             elif node.right is not None:
#                 print('right', node.right.val)
#                 q.append((node.right, True))
#             elif node.left is not None:
#                 print('left', node.left.val)
#                 q.append((node.left, True))
#
#         print(answer)
#         return answer
