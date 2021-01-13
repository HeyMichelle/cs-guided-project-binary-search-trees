"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def maxDepth(self):
        right_height = 0
        left_height = 0

        if self.right:
            right_height = self.maxDepth()

        if self.left:
            left_height = self.maxDepth(t)
                #1              #1              #0
        largest_height = max(right_height, left_height)

        return 1 + largest_height # this will do recursion to the right again
        # does not work if maybe left > right where 5 > 7
        # if there are children, find out what their depth is first - recursion


        # this says how long is your right side
        # now you must search the left side. Which is longer?
        # to find a max depth you need to find the longest path from root to furthest leaf node ( none x 2)
        # choose the longest one


# # Plan
#     # if it was 1, then there should be = 1
#       ? self = 1?
#   
#             5
#            /  \
#         None    7 (max depth)
#     # if no left or right, return 1
#     # there is theoretically max depth on node 7 (no trees/nodes at end)